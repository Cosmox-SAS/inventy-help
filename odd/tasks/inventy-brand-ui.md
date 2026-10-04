# Inventy brand UI

## Objective
Align the help center with the verified mobile brand theme and official logo.

## Authorization and scope
Local UI implementation only; no push, deployment, remote credentials, or mobile edits.
Preserve articles, navigation, review notices and pending screenshot markers.

## Plan
- [x] T1 Apply mobile-derived branding and official logo, then validate the documentation build and responsive light/dark presentation.

## Routing
T1: delegated direct; multi-file styling and preparation require one bounded writer.
Allowed surfaces: mkdocs.yml, docs/assets/stylesheets/ayuda.css, docs/index.md, docs/assets/brand/inventy-logo.svg.

## Acceptance and checks
Use verified orange/neutral tokens, Inter, and the unchanged official SVG.
Keep Colombian Spanish UI copy, readable contrast, keyboard focus and responsive navigation.
Run .venv/bin/python scripts/build_docs.py and git diff --check.
Inspect desktop/mobile and light/dark locally; record unavailable visual proof honestly.
No meaningful deterministic RED exists for this passive styling change; use build and visual checks.

## Delivery
Forecast: 100–180 authored changed lines; strategy ask-on-risk.
One work-unit commit on codex/inventy-brand-ui. No push or PR authorization.
Review switch: on (global). Base boundary: 6def7690eb559af477e79187d553a13c4cc03205.

## Progress
Implementation commit: 8aea3d9 (221 additions, 21 deletions; 242 authored lines).
Writer and independent verifier: build passed, 69 articles checked, 12 tests passed, strict MkDocs build passed; diff check passed.
Independent visual check: desktop 1280 and mobile 390, light/dark, mobile navigation drawer; no clipped logo or horizontal overflow.
Fixed active-tab selector after verification; final build against 8aea3d9 passed and generated markup matches.
Parent spot checks: git diff --check and byte-identical SVG comparison passed.
Native assessment: medium, under_budget (review_due=false); no review consent or receipt generated. Initial assessments refused undeclared unrelated untracked inventory; canonical inventory obtained and explicitly excluded.
No push, PR or deployment. Existing .atl and .codegraph kept intact.
Next step: user reviews local design; publishing requires separate authorization.
