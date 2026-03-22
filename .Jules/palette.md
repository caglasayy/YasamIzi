## 2024-05-18 - Flutter Web a11y & NoScript requirements
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback in `frontend/web/index.html` since Flutter requires JS to run.
**Action:** Always ensure Flutter Web projects include `lang` attribute on the `<html>` tag and a `<noscript>` tag for users with JS disabled in the entry HTML file.
