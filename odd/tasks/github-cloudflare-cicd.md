# GitHub and Cloudflare Pages CI/CD

## Objective
Validate documentation on GitHub PRs and publish previews and main through Cloudflare Pages in Cosmox_sas. Run validation in the Pages build itself so failures stop deployment. The original CI/CD task did not include a custom domain, paid plan, token creation or broad repository access; custom-domain documentation is tracked in `odd/tasks/custom-domain-documentation.md`.

## Authorization
User authorized Cosmox-SAS/inventy-help connection using current browser sessions; explicitly approved extending existing Cloudflare GitHub app to only this repo. Existing three repositories preserved.

## Tasks
- [x] T1: Add shared checked build command and GitHub workflow configuration, Python version, deployment documentation and tests.
- [x] T2: Configure Pages project inventy-help, main production, preview builds, site output; verify deployment after authorized publication.

## Route and delivery
Delegated direct T1: multi-file preparation/writer trigger. Parent UI T2: authorized configuration. Delivery ask-on-risk; forecast 200 authored lines for CI/CD. User later approved one PR including the earlier WebP migration with a size exception.

## Checks
- Shared build fails closed on validator/tests/build errors.
- Existing eight converter tests and docs validation/strict build pass.
- Automated conversion runs only in explicitly ephemeral CI checkout, never commits source or uses credentials. Source CLI remains manual locally.
- Production main, previews and build output verified in Pages UI.
- No push/merge without authorization for exact branch/session.

## Completion evidence
- The shared `scripts/build_docs.py` uses CI-only screenshot optimization followed by article checks, unit tests and strict MkDocs build. The default local command does not convert source images. Before publication, 12 tests, checks for 69 documentation files, the shared build and `git diff --check` passed; public CLI tests observed RED before implementation and GREEN afterward.
- User approved one PR including the WebP migration and CI/CD with a size exception. Commit `db6e1049908e732478784ac2bd7b6a0b2a88887e` was published on `codex/lossless-webp-screenshots`; [PR #1](https://github.com/Cosmox-SAS/inventy-help/pull/1) was opened with explicit approval to proceed without an issue. Native review did not complete because untracked-selection submission returned `invalid_request`; no native approval is claimed.
- User later authorized merging PR #1 and activating `main` deployments. The merge is `6ee7b93424f7f8dfc828e50347e6d0a7d3ae10a0`; GitHub main Actions run `37232593156` succeeded at that SHA. Cloudflare Pages project `inventy-help` in Cosmox_sas published `main` in deployment `75361095-5138-491f-adee-ea84c3e2c667` with Python 3.12, `site` output, automatic production deployment and previews enabled for non-production branches.
- Chrome loaded https://inventy-help.pages.dev/, search found the crear-producto article, and a WebP lightbox opened. Public command-line probes returned 403/1010, so browser verification was used as the availability proof. Preview configuration was verified, but a real PR preview has not yet been tested.

## Remaining check
Verify the first actual PR preview when a new PR is opened. The later custom domain and its documentation belong to `odd/tasks/custom-domain-documentation.md`.
