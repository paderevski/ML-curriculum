(() => {
  const components = Array.from(
    document.querySelectorAll("[data-notebook-links]"),
  );

  if (components.length === 0) {
    return;
  }

  let openComponent = null;
  const hoverCloseTimers = new WeakMap();

  function getParts(component) {
    return {
      button: component.querySelector(".notebook-links__label"),
      popover: component.querySelector(".notebook-links__actions"),
    };
  }

  function clearCloseTimer(component) {
    const timerId = hoverCloseTimers.get(component);
    if (!timerId) {
      return;
    }

    window.clearTimeout(timerId);
    hoverCloseTimers.delete(component);
  }

  function scheduleClose(component) {
    clearCloseTimer(component);

    const timerId = window.setTimeout(() => {
      closeComponent(component);
      hoverCloseTimers.delete(component);
    }, 120);

    hoverCloseTimers.set(component, timerId);
  }

  function closeComponent(component) {
    if (!component) {
      return;
    }

    clearCloseTimer(component);

    const { button, popover } = getParts(component);
    if (!button || !popover) {
      return;
    }

    button.setAttribute("aria-expanded", "false");
    popover.hidden = true;

    if (openComponent === component) {
      openComponent = null;
    }
  }

  function openCurrent(component) {
    if (openComponent && openComponent !== component) {
      closeComponent(openComponent);
    }

    const { button, popover } = getParts(component);
    if (!button || !popover) {
      return;
    }

    button.setAttribute("aria-expanded", "true");
    popover.hidden = false;
    openComponent = component;
  }

  components.forEach((component) => {
    const { button, popover } = getParts(component);
    if (!button || !popover) {
      return;
    }

    button.addEventListener("click", (event) => {
      event.preventDefault();
      clearCloseTimer(component);

      if (openComponent === component && !popover.hidden) {
        closeComponent(component);
        return;
      }

      openCurrent(component);
    });

    component.addEventListener("mouseenter", () => {
      clearCloseTimer(component);
      openCurrent(component);
    });

    component.addEventListener("mouseleave", () => {
      scheduleClose(component);
    });

    component.addEventListener("focusin", () => {
      clearCloseTimer(component);
      openCurrent(component);
    });

    component.addEventListener("focusout", (event) => {
      if (component.contains(event.relatedTarget)) {
        return;
      }

      scheduleClose(component);
    });

    component.addEventListener("keydown", (event) => {
      if (event.key !== "Escape") {
        return;
      }

      closeComponent(component);
      button.focus();
    });
  });

  document.addEventListener("click", (event) => {
    if (!openComponent) {
      return;
    }

    if (openComponent.contains(event.target)) {
      return;
    }

    closeComponent(openComponent);
  });
})();
