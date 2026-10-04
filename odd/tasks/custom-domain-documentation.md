# Custom domain documentation

## Objective and authorization
Synchronize README, AGENTS.md, canonical URL and deployment references with https://ayuda.inventy.com.co/. User authorized publishing these updates in a new PR to main, not merging it. Preserve historical Pages URLs as fallback/evidence where appropriate.

## Scope and route
- Include pending AGENTS.md and prior feature completion records.
- Delegated direct: multiple documentation/config files and preparation trigger.
- No workflow/code changes, DNS redirects, paid services or credentials.
- Base: 6ee7b93424f7f8dfc828e50347e6d0a7d3ae10a0.
- Branch: codex/docs-custom-domain.
- Delivery: ask-on-risk; forecast 180 authored lines, single PR.

## Tasks
- [x] T1: Update project guidance and README with active domain/CI-CD, preserve history accurately, verify canonical/sitemap, commit and open PR.

## Acceptance and checks
- README describes configured production, PR previews, shared build, logs, retry and rollback without secrets or invented gates.
- AGENTS.md identifies the production domain and source conventions.
- mkdocs.yml site_url uses custom domain.
- Old hostname remains only where appropriate as fallback, DNS target or historical evidence.
- Shared local build: .venv/bin/python scripts/build_docs.py; git diff --check.
- Passive documentation/config URL adjustment has no meaningful runnable RED; structural checks and existing integration build apply.
- Hosted CI and preview URL verified when PR opened.

## Progress and next step
Domain already loaded over HTTPS in Chrome before this work. README and AGENTS now identify the production domain and hosting workflow; earlier CI/CD and screenshot task records now distinguish historical pending states from the completed merge and deployment. The local `site_url` points to the production domain. Writer checks: `.venv/bin/python scripts/build_docs.py` passed (12 tests and strict MkDocs build), `git diff --check` passed, and generated homepage canonical and sitemap URLs use `https://ayuda.inventy.com.co/`. No meaningful runnable RED exists for this documentation/URL update. Parent readback, commit, assessment, PR creation and hosted CI/preview checks are complete; see delivery evidence below. No main merge is authorized.

## Delivery evidence
- Implementation commit: 994af412d080e73833629389833e1cc48603081d (140 authored changed lines).
- Independent verifier confirmed 69 documents, 12 tests, strict build, all canonical/sitemap URLs and diff checks.
- Native assessment: medium, under_budget; no review due for this slice.
- PR: https://github.com/Cosmox-SAS/inventy-help/pull/2 (open, not merged).
- GitHub validation and Cloudflare Pages checks passed for 994af41.
- First preview verified in Chrome: https://9354d706.inventy-help.pages.dev/; rendered homepage and canonical https://ayuda.inventy.com.co/.
- Next step: user review and explicit merge authorization. Production receives the canonical change only after merge.
