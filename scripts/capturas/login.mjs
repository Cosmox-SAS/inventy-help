#!/usr/bin/env node
/**
 * Inicio de sesión manual para el robot de capturas.
 *
 * Abre una ventana de Chrome en la página de inicio de sesión del ambiente demo.
 * Tú inicias sesión a mano; el script guarda solo la sesión (cookies) en
 * .auth-capturas.json (no se versiona) para que `npm run capturas` la reutilice.
 * Así la contraseña nunca queda escrita en ningún archivo.
 *
 * Uso: npm run capturas:login
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright';

const RAIZ = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const ENV = path.join(RAIZ, '.env.capturas');
const SESION = path.join(RAIZ, '.auth-capturas.json');

const url = (fs.existsSync(ENV) ? fs.readFileSync(ENV, 'utf8') : '').match(/^INVENTY_DEMO_URL=(.+)$/m)?.[1]?.trim().replace(/\/+$/, '');
if (!url) {
    console.error('✗ Falta INVENTY_DEMO_URL en .env.capturas');
    process.exit(1);
}

const navegador = await chromium.launch({ channel: 'chrome', headless: false }).catch(() => chromium.launch({ headless: false }));
const contexto = await navegador.newContext({ viewport: { width: 1440, height: 900 }, locale: 'es-CO' });
const page = await contexto.newPage();
await page.goto(`${url}/login`);

console.log('➜ Inicia sesión en la ventana de Chrome que se abrió (tienes 15 minutos).');
await page.waitForURL((u) => !/\/(login|two-factor-challenge)/.test(u.pathname), { timeout: 15 * 60_000 });
await page.waitForLoadState('networkidle').catch(() => {});

const empresa = new URL(page.url()).pathname.split('/').filter(Boolean)[0] ?? '';
const titulo = await page.title();
await contexto.storageState({ path: SESION });
fs.chmodSync(SESION, 0o600);
await navegador.close();

console.log(`✓ Sesión guardada en ${path.relative(RAIZ, SESION)} (no se sube a Git).`);
console.log(`  Empresa en la URL: ${empresa || '(ninguna)'}  ·  Página: ${titulo}`);
