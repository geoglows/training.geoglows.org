/*
 * Mobile sidebar behavior for the readthedocs theme.
 *
 * The theme closes the sidebar on every click on a nav link, including the section labels and the
 * current page's link, which only expand or collapse part of the menu. Here those clicks toggle
 * the menu and leave the sidebar open; links that go somewhere still close it. The sidebar also
 * closes from its close button, a tap on the dimmed page behind it, or Escape.
 *
 * Listens on window in the capture phase so it runs before the theme's jQuery handlers on document.
 */
(function () {
  function sidebar() {
    return document.querySelector("[data-toggle='wy-nav-shift'].wy-nav-side");
  }

  function setOpen(open) {
    document.querySelectorAll("[data-toggle='wy-nav-shift']").forEach(function (el) {
      el.classList.toggle("shift", open);
    });
  }

  function isOpen() {
    var nav = sidebar();
    return !!nav && nav.classList.contains("shift");
  }

  window.addEventListener("click", function (e) {
    var target = e.target;

    if (target.closest(".geo-nav-close")) {
      e.preventDefault();
      e.stopPropagation();
      setOpen(false);
      return;
    }

    // A tap anywhere on the page behind the open sidebar (including the menu button) closes it.
    if (isOpen() && target.closest(".wy-nav-content-wrap")) {
      e.preventDefault();
      e.stopPropagation();
      setOpen(false);
      return;
    }

    // The expand buttons the theme adds already stop propagation, so leave them alone.
    if (target.closest("button.toctree-expand")) return;

    var link = target.closest(".wy-menu-vertical ul li a");
    if (!link) return;
    var href = link.getAttribute("href");
    if (href !== null && href !== "#") return;

    // Section label or current page: toggle its submenu and keep the sidebar open.
    e.preventDefault();
    e.stopPropagation();
    if (window.SphinxRtdTheme && window.jQuery) {
      window.SphinxRtdTheme.Navigation.toggleCurrent(window.jQuery(link));
    }
  }, true);

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && isOpen()) setOpen(false);
  });
})();
