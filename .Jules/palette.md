## 2026-05-01 - [Flutter Web Accessibility Basics]
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback in `frontend/web/index.html`.
**Action:** Always check `index.html` for basic accessibility tags when working on Flutter web apps.
