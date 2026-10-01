#!/usr/bin/env node
/**
 * Explorador de pantallas para escribir recorridos de captura.
 *
 * Abre una ruta del ambiente demo con la sesión guardada, toma una foto en
 * .logs/explorar/ y lista los botones, enlaces, campos y textos visibles.
 * Opcionalmente ejecuta acciones de "solo abrir" antes (clics en botones que
 * abren ventanas), para inspeccionar modales.
 *
 * Uso:
 *   node scripts/capturas/explorar.mjs /{tenant}/cash/registers
 *   node scripts/capturas/explorar.mjs /{tenant}/cash/registers --abrir 'button:has-text("Nueva caja")'
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const SESION = path.join(RAIZ, '.auth-capturas.json');
const DIR = path.join(RAIZ, '.logs/explorar');
const env = Object.fromEntries(
    fs.readFileSync(path.join(RAIZ, '.env.capturas'), 'utf8').split('\n').map((l) => l.match(/^([A-Z_]+)=(.*)$/)).filter(Boolean).map((m) => [m[1], m[2].trim()]),
);
const base = env.INVENTY_DEMO_URL.replace(/\/+$/, '');

const args = process.argv.slice(2);
const ruta = args[0];
const abrir = [];
for (let i = 1; i < args.length; i++) if (args[i] === '--abrir') abrir.push(args[++i]);

const navegador = await chromium.launch({ channel: 'chrome' }).catch(() => chromium.launch());
const contexto = await navegador.newContext({ storageState: SESION, viewport: { width: 1440, height: 900 }, locale: 'es-CO' });
const page = await contexto.newPage();
await page.goto(`${base}/`, { waitUntil: 'networkidle' });
const tenant = env.INVENTY_DEMO_TENANT || new URL(page.url()).pathname.split('/').filter(Boolean)[0];
await page.goto(`${base}/${ruta.replace(/^\/+/, '').replaceAll('{tenant}', tenant)}`, { waitUntil: 'networkidle' });
for (const sel of abrir) {
    await page.locator(sel).first().click();
    await page.waitForTimeout(900);
}
await page.waitForTimeout(600);

fs.mkdirSync(DIR, { recursive: true });
const nombre = (ruta + abrir.join('_')).replace(/[^a-z0-9]+/gi, '_').slice(0, 80);
const foto = path.join(DIR, `${nombre}.png`);
await page.screenshot({ path: foto, fullPage: true });

const datos = await page.evaluate(() => {
    const visible = (el) => !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length);
    const ambito = document.querySelector('[role="dialog"]') ?? document.body;
    const texto = (el) => (el.innerText || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 60);
    return {
        url: location.pathname + location.search,
        dialogo: !!document.querySelector('[role="dialog"]'),
        titulos: [...ambito.querySelectorAll('h1,h2,h3,legend')].filter(visible).map(texto).filter(Boolean),
        botones: [...ambito.querySelectorAll('button,a[href],[role="button"],[role="tab"]')].filter(visible).map((el) => `${el.tagName.toLowerCase()}${el.getAttribute('type') === 'submit' ? '[submit]' : ''}${el.dataset.testid ? `[data-testid=${el.dataset.testid}]` : ''}${el.getAttribute('aria-label') ? `[aria-label="${el.getAttribute('aria-label')}"]` : ''}: ${texto(el)}`).filter((t) => !t.endsWith(': ') || t.includes('aria-label')),
        campos: [...ambito.querySelectorAll('input,select,textarea,[role="combobox"]')].filter(visible).map((el) => {
            const id = el.id ? `#${el.id}` : '';
            const label = el.id ? document.querySelector(`label[for="${el.id}"]`)?.innerText?.trim() : el.closest('div')?.querySelector('label')?.innerText?.trim();
            return `${el.tagName.toLowerCase()}${id}${el.name ? `[name=${el.name}]` : ''}${el.placeholder ? `[placeholder="${el.placeholder}"]` : ''}${el.getAttribute('role') ? `[role=${el.getAttribute('role')}]` : ''} ← ${label ?? ''}`;
        }),
        etiquetas: [...ambito.querySelectorAll('label')].filter(visible).map(texto).filter(Boolean),
    };
});
console.log(JSON.stringify({ foto: path.relative(RAIZ, foto), ...datos }, null, 1));
await navegador.close();
