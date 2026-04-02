## 2024-04-02 - Flutter Web Accessibility Baseline
**Learning:** Flutter Web apps mount into an empty `index.html`, which often lacks basic HTML-level accessibility features like `lang` attributes for screen readers and `<noscript>` fallbacks for when JS fails or is disabled.
**Action:** Always verify `frontend/web/index.html` for base accessibility tags (`lang` attribute, `<noscript>` block) before looking into widget-level accessibility in Flutter Web projects.
