# SEO metadata

## Objective and authorization
Implement meta titles/descriptions, social preview image, favicon, sitemap and robots.txt locally. User supplied Android SVG as image data. No remote publishing authorized.

## Scope and decisions
Keep existing Material titles/descriptions/canonical and MkDocs sitemap; add per-page OpenGraph/Twitter tags and one shared branded 1200x630 PNG. Copy supplied official icon unchanged as SVG favicon. robots.txt allows crawling and references canonical production sitemap. Preserve light-default palette and all review notices/articles.

## Tasks
- [x] T1 Implement SEO assets/metadata and deterministic rendered-output tests.

## Routing and surfaces
Delegated direct: multi-file logic and test-first output checks.
mkdocs.yml; overrides/main.html; docs/assets/brand/favicon.svg; docs/assets/brand/social-preview.png; docs/robots.txt; tests/test_seo_metadata.py.

## Acceptance and verification
Observe RED for new metadata/asset/robots assertions, then GREEN. Run .venv/bin/python scripts/build_docs.py and git diff --check. Verify canonical absolute metadata URLs, escaping, image 1200x630 and favicon, sitemap and robots output. Inspect composed image and local preview.

## Delivery
Forecast 150–250 authored lines excluding binary PNG. Strategy ask-on-risk. Work-unit commit on codex/inventy-brand-ui; preserve unrelated untracked .atl/.codegraph. Base boundary 1419d6a83c65824b1b7d301d22c215d92d190ed9. RDD on globally. No push or deployment.

## Progress
Implemented in 39a2c34: 228 additions, 4 deletions across six files (232 authored lines, PNG binary excluded).
Observed RED then GREEN for metadata assertions and the 404 canonical URL edge case. Final build: 69 articles, 16 tests, strict MkDocs build passed; git diff --check passed.
Independent verifier checked all 69 rendered index pages, sitemap and robots, unchanged official favicon and 1200x630 social image. Minor 404 empty URL tags found and fixed; final tests passed.
Home title duplication fixed. Light-default palette preserved in commit.
Parent checks: unchanged favicon comparison and diff check passed; local preview serves social tags.
Native assessment medium, under_budget (review_due=false), no review receipt issued. Unrelated untracked inventory explicitly excluded after canonical inventory read.
Environment limitation: existing .venv runs Python 3.9.6 rather than prescribed 3.12; Python 3.12 verification not performed.
Development server rewrites site_url to localhost; production strict build metadata uses canonical domain.
No remote publishing; next step is local review and separate publication authorization.

