# Lossless WebP screenshots

## Objective and scope
Replace tracked screenshot PNGs with lossless WebP only when strictly smaller and decoded RGBA pixels match. Update exact references and screenshot validation; preserve PNGs otherwise. No deployment, remote operations or history rewrite.

## Constraints and delivery
- Original files may be deleted only after verified conversion and reference updates.
- Route: delegated direct; multi-file implementation and preparation trigger.
- Delivery: ask-on-risk; forecast 600 authored text lines plus binary replacements. Chain strategy pending before commit.
- Branch point: ae2bec2e616875aea0017fd37177baad852af047.
- RDD on; native assessment/review after work-unit commit.
- Memory mirror pending: Engram project association fails.

## Tasks
- [ ] T1: Implement safe lossless converter, validation compatibility and focused tests; migrate beneficial screenshots and references; document usage and wire CI tests.

## Acceptance and checks
- Conversion preserves decoded pixels and only replaces smaller files.
- Existing WebP collisions and conversion failures never delete originals.
- References remain valid; glightbox built output resolves images.
- Tests: python -m unittest discover -s tests -v.
- Validation: python scripts/check_docs.py.
- Integration: python -m mkdocs build --strict.
- Migration report records before/after sizes and converted/retained counts.
- Test first at the user-approved file conversion/reference seam: observe RED then GREEN.

## Progress
Exploration and implementation complete; T1 remains open pending parent spot check and work-unit commit.
- Test-first: four initial tests failed before the converter/validator existed; the pending-manifest compatibility test also failed before its fix.
- Migrated 226 tracked PNGs to smaller, decoded-RGBA-identical WebP; retained 0. Screenshot bytes: 50,031,363 → 17,521,112 (32,510,251 saved). Rechecked all 226 against the Git HEAD PNG bytes.
- Updated exact Markdown image references; 226 built image sources and 226 glightbox hrefs resolve. The existing PNG-based pending manifest remains valid through dual-suffix matching in the validator.
- Checks passed: `.venv/bin/python -m unittest discover -s tests -v` (8 tests), `.venv/bin/python scripts/check_docs.py` (69 files), `.venv/bin/python -m mkdocs build --strict`. System Python lacked MkDocs, so an ignored local `.venv` was created from `requirements.txt`.
- Independent verification prompted a safety correction: animated and metadata/profile-bearing PNGs are now retained, as are PNGs with live Markdown/HTML references that the exact-link rewrite cannot update. New tests observed RED before the correction and GREEN afterward; existing 226 originals had no metadata, animation, or non-pixel PNG chunks.
- No commit, push, deployment, or history rewrite. Delivery strategy remains pending before commit because the authored text diff exceeds the ~400-line budget.

## Next step
Parent independently spot-checks, resolves delivery strategy before commit, then native review as applicable.

## Delivery authorization
User approved one PR including migration and CI/CD with size exception, publish branch codex/lossless-webp-screenshots; no merge to main authorized.
