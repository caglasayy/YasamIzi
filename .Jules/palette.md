## 2026-04-11 - Flutter Web Accessibility HTML Tags
**Learning:** Flutter Web applications mount directly into an almost empty index.html. Screen readers need explicit HTML attributes (like `<html lang="tr">`) to target the correct language, and users without JavaScript enabled need a fallback message using `<noscript>` since the app won't load.
**Action:** Always ensure the entry `index.html` for Flutter web projects includes correct language attributes and `<noscript>` fallbacks for base level accessibility.
