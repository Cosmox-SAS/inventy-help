# Agent guidance for Inventy Help

This repository is the end-user help center for Inventy ERP, built with MkDocs Material. It is **not** the developer documentation for the ERP. Published articles are in `docs/`; internal editorial material is in `gestion/` and templates are in `plantillas/`.

## Start here

- Read `README.md` for the contributor workflow, `gestion/guia-de-estilo.md` for editorial rules, and the matching file in `plantillas/` before changing an article.
- Use Python 3.12 (`.python-version`). Set up a local environment with `python3 -m venv .venv` and `.venv/bin/pip install -r requirements.txt`; preview with `.venv/bin/mkdocs serve`.
- Run `.venv/bin/python scripts/build_docs.py` before handing off documentation changes. It checks articles, runs the Python unit tests, and builds MkDocs in strict mode. Do not use `--optimize-screenshots` locally; that flag is restricted to GitHub Actions and Cloudflare Pages builds.
- The generated `site/` directory is build output. Edit `docs/`, configuration, templates, or scripts instead of generated pages.

## Write user help

- Write published help in clear, professional Colombian Spanish for ERP users, not developers. Use the exact, verified labels users see in Inventy; do not invent buttons, fields, menus, or outcomes. Keep code, identifiers, and technical comments in English unless their existing context requires otherwise.
- Default to `plantillas/guia-rapida.md` (`tipo: rapida`). Use `plantillas/tutorial.md` only when the process needs context, and `plantillas/solucion-rapida.md` for troubleshooting. Follow the template's required headings and step format.
- Except for the home page, articles require front matter including `title`, `description`, `estado`, `tipo`, `modulo`, and a `revisado` date. `scripts/check_docs.py` is the source of truth for allowed values and validation rules.
- Add new articles to `nav` in `mkdocs.yml`; use relative links and real screenshot paths. Keep a quick guide's numbered `**Paso N.**` actions consecutive, with a screenshot under every step.
- If a behavior cannot be confirmed in the real interface, mark the specific uncertainty with `PENDIENTE DE VALIDACIÓN FUNCIONAL` and keep the article in a non-published state. Do not promote an article to `validado` or `publicado` without the human functional and editorial review described in `gestion/guia-de-estilo.md`.

## Screenshots and sensitive data

- Screenshots belong in `docs/assets/capturas/`; capture flows live in `scripts/capturas/guias/`. Use only the Inventy demo company, never real customer data. Keep `.env.capturas` and credentials out of Git. Never ask readers for passwords, PINs, verification codes, or full card details.
- Placeholder screenshots are tracked by `docs/assets/capturas/pendientes.txt`. Do not remove a pending marker or publish an article until the placeholder has been replaced and verified.
- `scripts/optimize_screenshots.py` is an explicit, source-mutating migration, not a routine validation step. It considers only PNGs already in Git's index: stage newly added PNGs before running it, then review and restage the converted images, removed PNGs, and article links. It preserves PNGs when conversion would be larger or could lose metadata, animation, or decoded pixels.

## CI and delivery

- Production is https://ayuda.inventy.com.co/, with `mkdocs.yml` `site_url` as its canonical URL. The Cloudflare Pages project is `inventy-help` in `Cosmox_sas`, connected to `Cosmox-SAS/inventy-help`; https://inventy-help.pages.dev/ remains an active alternate address without a redirect. Do not present the Pages hostname as the canonical site or assume that a configured PR preview has already been tested.
- `.github/workflows/docs-check.yml` validates pull requests and pushes to `main` through `scripts/build_docs.py --optimize-screenshots`. The Cloudflare Pages build command and production/preview configuration are documented in `README.md`; CI conversion occurs in the build checkout, not in the source branch.
- Pages publishes `main` automatically, and previews are enabled for non-production branches. Check the GitHub Actions run and the matching Cloudflare Pages deployment separately; an Actions success alone is not deployment proof. Generated canonical links and sitemap entries should use the production domain.
- Do not push, deploy, change Cloudflare settings, or use remote credentials without explicit authorization. Keep unrelated local changes intact. If asked to commit, use a Conventional Commit message without AI attribution.
