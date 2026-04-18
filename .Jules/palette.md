## 2026-04-18 - Base Accessibility Tags for Flutter Web
**Learning:** Flutter Web applications mount into an almost empty `index.html`. Basic accessibility requirements like setting the screen reader language (`lang` attribute on `<html>`) and providing a fallback for users without JavaScript (`<noscript>`) must be handled manually in the entry point file.
**Action:** Always check the root `index.html` for basic accessibility tags when working with Flutter Web projects.
