
## 2024-05-18 - Flutter Web Entry Point Accessibility
**Learning:** Flutter Web applications mount directly into an almost empty index.html, which means standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback since the whole app is JS-dependent.
**Action:** Always verify the root `web/index.html` file in Flutter Web projects to ensure baseline semantic HTML and JS-disabled fallbacks are present before working on deeper widget-level accessibility.
