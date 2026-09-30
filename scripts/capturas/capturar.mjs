#!/usr/bin/env node
/**
 * Capturas de pantalla automáticas del Centro de Ayuda Inventy.
 *
 * Entra al ambiente demo de Inventy con un usuario de prueba, recorre cada guía
 * definida en scripts/capturas/guias/*.yaml, resalta el elemento de cada paso y
 * guarda la imagen en docs/assets/capturas/<guía>/paso-<n>.png.
 *
 * Uso:
 *   npm run capturas                         # todas las guías
 *   npm run capturas -- pos/cierre-de-caja   # solo las que contengan ese texto
 *   npm run capturas -- --ver                # con el navegador visible
 *
 * Credenciales: archivo .env.capturas (no se versiona). Ver .env.capturas.example.
 *
 * Seguridad: por defecto NUNCA hace clic en botones que guardan datos
 * (Guardar, Confirmar, Crear, Validar, Aprobar…). Un paso solo puede hacerlo si
 * declara `guarda_datos: true` Y se corre con CAPTURAS_PERMITIR_GUARDAR=1.
 * Para botones que solo abren una ventana (ej. "Cerrar caja" en la barra del
 * POS abre el formulario), usa la acción `abrir` en lugar de `clic`.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';
import YAML from 'yaml';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const DIR_GUIAS = path.join(RAIZ, 'scripts/capturas/guias');
const DIR_CAPTURAS = path.join(RAIZ, 'docs/assets/capturas');
const PENDIENTES = path.join(DIR_CAPTURAS, 'pendientes.txt');
const REPORTE = path.join(RAIZ, 'gestion/capturas-reporte.md');

const VIEWPORTS = {
    escritorio: { width: 1440, height: 900 },
    celular: { width: 390, height: 844 },
};
const BOTON_QUE_GUARDA =
    /^(guardar|confirmar|crear|validar|aprobar|recibir|finalizar|emitir|registrar|enviar|eliminar|anular|realizar|solicitar|rechazar|reabrir|cerrar caja|abrir caja|unirme|invitar|importar|pagar|cobrar)/i;
const ESPERA_MS = 10_000;

// ── Configuración ──────────────────────────────────────────────────────────
function cargarEnv() {
    const archivo = path.join(RAIZ, '.env.capturas');
    if (!fs.existsSync(archivo)) {
        console.error('✗ Falta .env.capturas. Copia .env.capturas.example y completa URL, correo y contraseña del usuario demo.');
        process.exit(1);
    }
    const env = {};
    for (const linea of fs.readFileSync(archivo, 'utf8').split('\n')) {
        const m = linea.match(/^\s*([A-Z_]+)\s*=\s*(.*)\s*$/);
        if (m) env[m[1]] = m[2].replace(/^['"]|['"]$/g, '');
    }
    for (const clave of ['INVENTY_DEMO_URL', 'INVENTY_DEMO_EMAIL', 'INVENTY_DEMO_PASSWORD']) {
        if (!env[clave]) {
            console.error(`✗ Falta ${clave} en .env.capturas`);
            process.exit(1);
        }
    }
    env.INVENTY_DEMO_URL = env.INVENTY_DEMO_URL.replace(/\/+$/, '');
    return env;
}

function cargarGuias(filtro) {
    return fs
        .readdirSync(DIR_GUIAS)
        .filter((f) => f.endsWith('.yaml'))
        .map((f) => ({ archivo: f, ...YAML.parse(fs.readFileSync(path.join(DIR_GUIAS, f), 'utf8')) }))
        .filter((g) => !filtro || g.guia.includes(filtro))
        .sort((a, b) => a.guia.localeCompare(b.guia));
}

// ── Acciones ───────────────────────────────────────────────────────────────
function localizar(page, selector) {
    return page.locator(selector).first();
}

async function sesion(page, env) {
    await page.goto(`${env.INVENTY_DEMO_URL}/login`, { waitUntil: 'networkidle' });
    await page.fill('input[name="email"]', env.INVENTY_DEMO_EMAIL);
    await page.fill('input[name="password"]', env.INVENTY_DEMO_PASSWORD);
    await Promise.all([page.waitForURL((u) => !u.pathname.endsWith('/login'), { timeout: 30_000 }), page.click('button[type="submit"]')]);
    await page.waitForLoadState('networkidle');
    const tenant = env.INVENTY_DEMO_TENANT || new URL(page.url()).pathname.split('/').filter(Boolean)[0];
    if (!tenant || tenant === 'admin') {
        throw new Error('El usuario demo no entró a una empresa. Define INVENTY_DEMO_TENANT en .env.capturas.');
    }
    return tenant;
}

async function irAlMenu(page, opcion) {
    await page.keyboard.press('Control+k');
    const buscador = page.getByPlaceholder('Buscar en el menú…');
    await buscador.waitFor({ timeout: ESPERA_MS });
    await buscador.fill(opcion);
    const exacta = page.getByRole('option', { name: opcion, exact: true }).first();
    const parcial = page.getByRole('option', { name: opcion, exact: false }).first();
    await parcial.waitFor({ timeout: ESPERA_MS });
    await ((await exacta.count()) ? exacta : parcial).click();
    await page.waitForLoadState('networkidle');
}

async function clic(page, selector, paso, puedeGuardar) {
    const objetivo = localizar(page, selector);
    await objetivo.waitFor({ timeout: ESPERA_MS });
    const texto = ((await objetivo.innerText().catch(() => '')) || selector).trim();
    if (BOTON_QUE_GUARDA.test(texto) && !(paso.guarda_datos && puedeGuardar)) {
        throw new Error(`Bloqueado: "${texto}" guardaría datos. Marca el paso con guarda_datos: true y usa CAPTURAS_PERMITIR_GUARDAR=1.`);
    }
    await objetivo.click();
    await page.waitForLoadState('networkidle').catch(() => {});
}

async function resaltar(page, selector) {
    const objetivo = localizar(page, selector);
    await objetivo.waitFor({ timeout: ESPERA_MS });
    await objetivo.scrollIntoViewIfNeeded();
    await objetivo.evaluate((el) => {
        el.dataset.capturaResaltado = '1';
        el.style.setProperty('outline', '3px solid #f59e0b', 'important');
        el.style.setProperty('outline-offset', '3px', 'important');
        el.style.setProperty('box-shadow', '0 0 0 9999px rgba(15, 23, 42, 0.12)', 'important');
        el.style.setProperty('border-radius', getComputedStyle(el).borderRadius || '6px');
        el.style.setProperty('position', getComputedStyle(el).position === 'static' ? 'relative' : getComputedStyle(el).position);
        el.style.setProperty('z-index', '2147483000', 'important');
    });
}

async function quitarResaltado(page) {
    await page.evaluate(() => {
        for (const el of document.querySelectorAll('[data-captura-resaltado]')) {
            for (const p of ['outline', 'outline-offset', 'box-shadow', 'z-index']) el.style.removeProperty(p);
            delete el.dataset.capturaResaltado;
        }
    });
}

async function ejecutarPaso(page, paso, ctx) {
    const url = (u) => `${ctx.env.INVENTY_DEMO_URL}/${u.replace(/^\/+/, '').replaceAll('{tenant}', ctx.tenant)}`;
    for (const accion of paso.acciones ?? []) {
        const [tipo, valor] = Object.entries(accion)[0];
        switch (tipo) {
            case 'ir':
                await page.goto(url(valor), { waitUntil: 'networkidle' });
                break;
            case 'menu':
                await irAlMenu(page, valor);
                break;
            case 'clic':
                await clic(page, valor, paso, ctx.puedeGuardar);
                break;
            case 'abrir': {
                // Clic en un botón que SOLO abre una ventana o menú (no guarda nada).
                const objetivo = localizar(page, valor);
                await objetivo.waitFor({ timeout: ESPERA_MS });
                await objetivo.click();
                break;
            }
            case 'llenar_credenciales':
                await localizar(page, 'input[name="email"]').fill(ctx.env.INVENTY_DEMO_EMAIL);
                await localizar(page, 'input[name="password"]').fill('••••••••');
                break;
            case 'llenar':
                for (const [sel, texto] of Object.entries(valor)) await localizar(page, sel).fill(String(texto));
                break;
            case 'escribir':
                for (const [sel, texto] of Object.entries(valor)) await localizar(page, sel).pressSequentially(String(texto), { delay: 30 });
                break;
            case 'tecla':
                await page.keyboard.press(valor);
                break;
            case 'esperar':
                await localizar(page, valor).waitFor({ timeout: ESPERA_MS });
                break;
            case 'pausa':
                await page.waitForTimeout(Number(valor));
                break;
            default:
                throw new Error(`Acción desconocida: ${tipo}`);
        }
    }
    await page.waitForTimeout(400); // animaciones de modales y toasts
    if (paso.resaltar) await resaltar(page, paso.resaltar);
}

// ── Principal ──────────────────────────────────────────────────────────────
async function main() {
    const args = process.argv.slice(2);
    const visible = args.includes('--ver');
    const filtro = args.find((a) => !a.startsWith('--'));
    const env = cargarEnv();
    const puedeGuardar = process.env.CAPTURAS_PERMITIR_GUARDAR === '1';
    const guias = cargarGuias(filtro);
    if (!guias.length) {
        console.error(`✗ No hay guías con capturas${filtro ? ` que coincidan con "${filtro}"` : ''}.`);
        process.exit(1);
    }

    const navegador = await chromium.launch({ channel: 'chrome', headless: !visible }).catch(() => chromium.launch({ headless: !visible }));
    const pendientes = new Set(fs.existsSync(PENDIENTES) ? fs.readFileSync(PENDIENTES, 'utf8').split('\n').filter(Boolean) : []);
    const resultados = [];

    for (const guia of guias) {
        const contexto = await navegador.newContext({
            viewport: VIEWPORTS[guia.vista ?? 'escritorio'],
            deviceScaleFactor: 2,
            locale: 'es-CO',
            timezoneId: 'America/Bogota',
            colorScheme: 'light',
        });
        const page = await contexto.newPage();
        const ctx = { env, puedeGuardar, tenant: null };
        const dirGuia = path.join(DIR_CAPTURAS, guia.guia.replace(/\.md$/, ''));
        fs.mkdirSync(dirGuia, { recursive: true });
        console.log(`\n▶ ${guia.guia}`);

        try {
            // `sin_sesion: true` para guías de acceso (login, recuperar contraseña).
            ctx.tenant = guia.sin_sesion ? null : await sesion(page, env);
        } catch (error) {
            console.log(`  ✗ No se pudo iniciar sesión: ${error.message}`);
            resultados.push({ guia: guia.guia, paso: '—', ok: false, detalle: `Inicio de sesión: ${error.message}` });
            await contexto.close();
            continue;
        }

        for (const paso of guia.pasos) {
            const destino = path.join(dirGuia, `paso-${paso.paso}.png`);
            const relativo = path.relative(path.join(RAIZ, 'docs'), destino);
            if (paso.manual) {
                // Pantallas que el robot no puede alcanzar (correos, otra persona, app móvil).
                resultados.push({ guia: guia.guia, paso: paso.paso, ok: false, detalle: `Captura manual: ${paso.manual}` });
                console.log(`  · Paso ${paso.paso}: captura manual (${paso.manual})`);
                continue;
            }
            try {
                await ejecutarPaso(page, paso, ctx);
                const recorte = paso.recortar ? await localizar(page, paso.recortar).boundingBox() : null;
                await page.screenshot({
                    path: destino,
                    clip: recorte
                        ? { x: Math.max(recorte.x - 24, 0), y: Math.max(recorte.y - 24, 0), width: recorte.width + 48, height: recorte.height + 48 }
                        : undefined,
                    animations: 'disabled',
                });
                await quitarResaltado(page);
                pendientes.delete(relativo);
                resultados.push({ guia: guia.guia, paso: paso.paso, ok: true });
                console.log(`  ✓ Paso ${paso.paso}`);
            } catch (error) {
                const detalle = error.message.split('\n')[0];
                resultados.push({ guia: guia.guia, paso: paso.paso, ok: false, detalle });
                console.log(`  ✗ Paso ${paso.paso}: ${detalle}`);
                if (paso.detener_si_falla !== false) break; // los pasos siguientes dependen de este
            }
        }
        await contexto.close();
    }
    await navegador.close();

    fs.writeFileSync(PENDIENTES, [...pendientes].sort().join('\n') + (pendientes.size ? '\n' : ''));

    const ok = resultados.filter((r) => r.ok).length;
    const fallas = resultados.filter((r) => !r.ok);
    const lineas = [
        '# Reporte de capturas',
        '',
        `> Generado por \`npm run capturas\` el ${new Date().toLocaleString('es-CO')}. Ambiente: ${env.INVENTY_DEMO_URL}`,
        '',
        `**${ok}** capturas tomadas · **${fallas.length}** fallas · **${pendientes.size}** imágenes siguen pendientes.`,
        '',
        ...(fallas.length ? ['## Fallas', '', '| Guía | Paso | Detalle |', '|---|---|---|', ...fallas.map((f) => `| ${f.guia} | ${f.paso} | ${f.detalle.replaceAll('|', '/')} |`), ''] : []),
    ];
    fs.writeFileSync(REPORTE, lineas.join('\n'));
    console.log(`\n${ok} capturas tomadas, ${fallas.length} fallas. Reporte: ${path.relative(RAIZ, REPORTE)}`);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
