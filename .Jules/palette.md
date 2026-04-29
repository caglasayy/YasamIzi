## 2024-04-29 - Missing Accessibility Defaults in Flutter Web
**Learning:** Flutter Web applications mount into an almost empty index.html, meaning standard accessibility features like screen reader language targeting (`<html lang="tr">`) and `<noscript>` fallback are missing by default.
**Action:** Explicitly add `<html lang="tr">` and a `<noscript>` tag containing a helpful Turkish message to `frontend/web/index.html` to ensure basic accessibility.
