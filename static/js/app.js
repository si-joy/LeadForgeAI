document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.querySelector("[data-sidebar]");
  const overlay = document.querySelector("[data-sidebar-overlay]");
  const menuButton = document.querySelector("[data-sidebar-toggle]");

  const themeButton = document.querySelector("[data-theme-toggle]");
  const themeMenu = document.querySelector("[data-theme-menu]");

  function openSidebar() {
    sidebar?.classList.add("is-open");
    overlay?.classList.add("is-open");
  }

  function closeSidebar() {
    sidebar?.classList.remove("is-open");
    overlay?.classList.remove("is-open");
  }

  menuButton?.addEventListener("click", openSidebar);
  overlay?.addEventListener("click", closeSidebar);

  themeButton?.addEventListener("click", function (event) {
    event.stopPropagation();
    themeMenu?.classList.toggle("is-open");
  });

  document.querySelectorAll("[data-theme-option]").forEach(function (button) {
    button.addEventListener("click", function () {
      const theme = button.dataset.themeOption;

      LeadForgeTheme.set(theme);
      themeMenu?.classList.remove("is-open");
    });
  });

  document.addEventListener("click", function () {
    themeMenu?.classList.remove("is-open");
  });
});