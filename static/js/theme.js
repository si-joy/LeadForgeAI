(function () {
  const root = document.documentElement;
  const storageKey = "leadforge-theme";

  const systemQuery = window.matchMedia(
    "(prefers-color-scheme: dark)"
  );

  function getSystemTheme() {
    return systemQuery.matches ? "dark" : "light";
  }

  function getPreference() {
    return localStorage.getItem(storageKey) || "system";
  }

  function resolveTheme(preference) {
    return preference === "system"
      ? getSystemTheme()
      : preference;
  }

  function applyTheme(preference) {
    const theme = resolveTheme(preference);

    root.dataset.theme = theme;
    root.dataset.themePreference = preference;
  }

  function setTheme(preference) {
    localStorage.setItem(storageKey, preference);
    applyTheme(preference);

    document.dispatchEvent(
      new CustomEvent("leadforge:theme-changed", {
        detail: {
          preference,
          theme: resolveTheme(preference),
        },
      })
    );
  }

  systemQuery.addEventListener("change", function () {
    if (getPreference() === "system") {
      applyTheme("system");
    }
  });

  window.LeadForgeTheme = {
    get: getPreference,
    set: setTheme,
    apply: applyTheme,
  };

  applyTheme(getPreference());
})();