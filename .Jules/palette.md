## 2026-05-15 - HTML Language and JavaScript Fallback in Flutter Web
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback.
**Action:** Always add `lang` attribute to `<html>` and a `<noscript>` tag for JavaScript-disabled fallback in Flutter web entry points.
