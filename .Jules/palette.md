
## 2024-04-23 - Screen Reader Support and JS Fallbacks for Flutter Web
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback to inform users when JavaScript is disabled.
**Action:** Always verify `frontend/web/index.html` has explicit `lang` attribute and an accessible `<noscript>` element in Flutter Web projects.
