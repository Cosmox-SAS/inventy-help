# GitHub and Cloudflare Pages CI/CD

## Objective
Validate documentation on GitHub PRs and publish previews and main through Cloudflare Pages in Cosmox_sas. Run validation in the Pages build itself so failures stop deployment. No custom domain, paid plan, token creation or broad repository access.

## Authorization
User authorized Cosmox-SAS/inventy-help connection using current browser sessions; explicitly approved extending existing Cloudflare GitHub app to only this repo. Existing three repositories preserved.

## Tasks
- [ ] T1: Add shared checked build command and GitHub workflow configuration, Python version, deployment documentation and tests.
- [ ] T2: Configure Pages project inventy-help, main production, preview builds, site output; verify deployment after authorized publication.

## Route and delivery
Delegated direct T1: multi-file preparation/writer trigger. Parent UI T2: authorized configuration. Delivery ask-on-risk; forecast 200 authored lines for CI/CD; earlier WebP migration has unresolved >400-line delivery exception and no commit.

## Checks
- Shared build fails closed on validator/tests/build errors.
- Existing eight converter tests and docs validation/strict build pass.
- Automated conversion runs only in explicitly ephemeral CI checkout, never commits source or uses credentials. Source CLI remains manual locally.
- Production main, previews and build output verified in Pages UI.
- No push/merge without authorization for exact branch/session.

## Progress
GitHub app access saved; Pages repository inventory now includes inventy-help and the existing three landing repos. No Pages project created yet.

T1 implementation is staged in the working tree but not committed or checked off. The shared `scripts/build_docs.py` runs screenshot optimization only with an explicit flag in GitHub Actions or Cloudflare Pages CI, then document checks, tests, and strict MkDocs build. The default local command does not convert source images. GitHub Actions calls the shared command on pull requests and main; Pages uses the same command after dependency installation. Public CLI tests observed RED before implementation and GREEN afterward. Final local checks: 12 tests passed, 69 documentation files passed, shared build exited 0, and `git diff --check` exited 0. No CI or Pages deployment has run yet; parent must read back, decide commit boundary, and verify remote deployment in T2.

## Next step
Parent checks and commits T1 when appropriate, then Pages configuration and publication decision. Memory mirror pending write/readback.

## Parent verification and publication status
- Shared build implemented and independently checked: 12 tests, 69 docs checks and strict build pass. Parent reran 12 tests and diff check.
- Pages form prepared (not submitted): inventy-help.pages.dev, main, site output, Python 3.12, shared CI-only optimizing build command.
- Existing GitHub app access now includes inventy-help and preserves previous three repos.
- T1 remains open pending commit; T2 pending project creation and hosted verification.
- Publication requires source files to reach GitHub before Pages can run the new command. No push, PR or merge yet.

## Delivery authorization
User approved one PR including migration and CI/CD with size exception, publish branch codex/lossless-webp-screenshots; no merge to main authorized.
