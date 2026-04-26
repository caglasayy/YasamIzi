
## 2024-04-26 - Flutter Web Screen Reader & JavaScript Fallback
**Learning:** Flutter Web applications mount directly into an almost empty `index.html`. This means standard HTML-level accessibility features, such as screen reader language targeting (e.g., `lang="tr"`), require explicit manual addition to the `<html>` tag. Furthermore, since the app relies entirely on JavaScript, adding a `<noscript>` tag is crucial for fallback user experience when JavaScript is disabled or fails to load.
**Action:** Always check the `index.html` entry point for Flutter Web apps to ensure standard HTML accessibility attributes (like `lang`) and graceful fallbacks (`<noscript>`) are present, rather than assuming Flutter framework handles the root HTML document setup.
