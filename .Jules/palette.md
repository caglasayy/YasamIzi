## 2024-05-14 - HTML Language Attribute and Noscript Tag for Flutter Web
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback in `frontend/web/index.html`.
**Action:** Always check the root `index.html` in Flutter Web projects to ensure language attributes and noscript fallbacks are explicitly added, rather than relying on the framework to inject them.
