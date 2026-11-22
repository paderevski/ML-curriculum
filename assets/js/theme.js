// Theme behavior: mobile nav toggle + "On this page" table of contents.
(() => {
  // ── Mobile nav panel ───────────────────────────────────────────────────────
  // The Menu button lives in the sticky masthead; the nav it opens is the
  // sidebar, shown as a full-height panel under the masthead on small screens.
  const toggle = document.querySelector("[data-nav-toggle]");
  const sidebar = document.querySelector(".sidebar");
  if (toggle && sidebar) {
    const setOpen = (open) => {
      sidebar.classList.toggle("is-open", open);
      document.documentElement.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", String(open));
    };
    toggle.addEventListener("click", () => setOpen(!sidebar.classList.contains("is-open")));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && sidebar.classList.contains("is-open")) {
        setOpen(false);
        toggle.focus();
      }
    });
    // Same-page links (e.g. /#daily-assignments) don't navigate away, so close.
    sidebar.addEventListener("click", (e) => {
      if (e.target.closest("a")) setOpen(false);
    });
    // Back to desktop width: drop the panel state.
    window.matchMedia("(min-width: 1024px)").addEventListener("change", (e) => {
      if (e.matches) setOpen(false);
    });
  }

  // ── Wide inline math ───────────────────────────────────────────────────────
  // Inline equations can't wrap; on phones a long one would push the whole
  // page sideways. Give only the ones that overflow their own scrollbar.
  const markWideMath = () => {
    for (const m of document.querySelectorAll(".page__content mjx-container:not([display])")) {
      // Measure the rendered math itself (inline elements have no scrollWidth).
      m.classList.remove("mjx-wide");
      const box = m.parentElement.getBoundingClientRect();
      const r = m.getBoundingClientRect();
      if (r.width > box.width || r.right > box.right + 1) m.classList.add("mjx-wide");
    }
  };
  window.addEventListener("load", () => {
    window.MathJax?.startup?.promise?.then(markWideMath);
  });
  window.addEventListener("resize", () => window.MathJax?.startup && markWideMath());

  // ── Table of contents ──────────────────────────────────────────────────────
  // Built from h2/h3 headings with ids inside .page__content.
  const toc = document.querySelector("[data-toc]");
  if (!toc) return;
  const content = document.querySelector(".page__content");
  const headings = Array.from(content.querySelectorAll("h2[id], h3[id]"));
  if (headings.length === 0) {
    toc.closest(".page__toc").remove();
    document.querySelector(".page")?.classList.remove("page--with-toc");
    return;
  }

  const list = document.createElement("ul");
  list.className = "toc__list";
  const links = new Map();
  for (const h of headings) {
    const li = document.createElement("li");
    li.className = `toc__item toc__item--${h.tagName.toLowerCase()}`;
    const a = document.createElement("a");
    a.href = `#${h.id}`;
    a.textContent = h.textContent.trim();
    li.appendChild(a);
    list.appendChild(li);
    links.set(h, a);
  }
  toc.appendChild(list);

  // Highlight the section currently in view.
  let current = null;
  const setCurrent = (h) => {
    if (current === h) return;
    current?.classList.remove("is-current");
    current = links.get(h);
    current?.classList.add("is-current");
  };
  const onScroll = () => {
    const offset = 120;
    let active = headings[0];
    for (const h of headings) {
      if (h.getBoundingClientRect().top - offset <= 0) active = h;
      else break;
    }
    setCurrent(active);
  };
  document.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
})();
