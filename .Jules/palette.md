## 2024-05-18 - Added Language Attribute and Noscript Fallback
**Learning:** Flutter Web applications mount directly into an almost empty index.html, meaning standard accessibility features like screen reader language targeting require explicit HTML attributes (e.g., `<html lang="tr">`) and `<noscript>` tags for fallback.
**Action:** When working on Flutter web entry points, always ensure the root HTML document provides sufficient context for accessibility tools and fallback scenarios.
