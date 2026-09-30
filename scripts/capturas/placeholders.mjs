#!/usr/bin/env node
/**
 * Crea una imagen provisional ("Captura pendiente") por cada captura que citan
 * las guías y que todavía no existe. Así el sitio compila mientras se toman las
 * capturas reales con `npm run capturas`, que las reemplaza.
 *
 * Las imágenes provisionales quedan listadas en docs/assets/capturas/pendientes.txt;
 * scripts/check_docs.py impide publicar guías que aún las usen.
 *
 * Uso: npm run capturas:placeholders
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const DOCS = path.join(RAIZ, 'docs');
const PENDIENTES = path.join(DOCS, 'assets/capturas/pendientes.txt');
const IMAGEN = /!\[([^\]]*)\]\(([^)\s]+assets\/capturas\/[^)\s]+\.png)\)/g;

function archivosMd(dir) {
    return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
        const ruta = path.join(dir, e.name);
        return e.isDirectory() ? archivosMd(ruta) : e.name.endsWith('.md') ? [ruta] : [];
    });
}

const faltantes = [];
for (const md of archivosMd(DOCS)) {
    for (const [, alt, src] of fs.readFileSync(md, 'utf8').matchAll(IMAGEN)) {
        const destino = path.resolve(path.dirname(md), src);
        if (!fs.existsSync(destino)) faltantes.push({ destino, alt });
    }
}

const pendientes = new Set(fs.existsSync(PENDIENTES) ? fs.readFileSync(PENDIENTES, 'utf8').split('\n').filter(Boolean) : []);

if (faltantes.length) {
    const navegador = await chromium.launch({ channel: 'chrome' }).catch(() => chromium.launch());
    const page = await navegador.newPage({ viewport: { width: 1440, height: 900 } });
    for (const { destino, alt } of faltantes) {
        const texto = alt.replace(/[<>&]/g, '');
        await page.setContent(`
            <body style="margin:0;height:100vh;display:flex;align-items:center;justify-content:center;
                         background:repeating-linear-gradient(45deg,#f1f5f9,#f1f5f9 24px,#e2e8f0 24px,#e2e8f0 48px);
                         font-family:-apple-system,Segoe UI,Roboto,sans-serif;color:#475569">
              <div style="text-align:center;background:#fff;border:2px dashed #94a3b8;border-radius:16px;padding:48px 64px;max-width:900px">
                <div style="font-size:56px">📷</div>
                <div style="font-size:34px;font-weight:700;margin:12px 0">Captura pendiente</div>
                <div style="font-size:24px">${texto}</div>
              </div>
            </body>`);
        fs.mkdirSync(path.dirname(destino), { recursive: true });
        await page.screenshot({ path: destino });
        pendientes.add(path.relative(DOCS, destino));
    }
    await navegador.close();
}

fs.mkdirSync(path.dirname(PENDIENTES), { recursive: true });
fs.writeFileSync(PENDIENTES, [...pendientes].sort().join('\n') + (pendientes.size ? '\n' : ''));
console.log(`${faltantes.length} imagen(es) provisional(es) creada(s). Pendientes en total: ${pendientes.size}.`);
