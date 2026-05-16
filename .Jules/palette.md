## 2026-05-16 - Flutter Web Accessibility Basics
**Learning:** Flutter web applications mount into an empty index.html, meaning basic accessibility like screen reader language targeting and noscript fallbacks require explicit HTML configuration rather than Dart code.
**Action:** Added lang="tr" to <html> and a <noscript> tag in index.html to ensure screen readers use the correct pronunciation and users without JS enabled receive a clear message.
