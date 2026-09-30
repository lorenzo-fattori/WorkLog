document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#entry-form");
  const hours = document.querySelector("#hours");

  form?.addEventListener("submit", (event) => {
    const value = Number(hours.value);
    if (!Number.isFinite(value) || value <= 0 || value > 24) {
      event.preventDefault();
      hours.focus();
    }
  });

  document.querySelectorAll(".flash").forEach((message) => {
    window.setTimeout(() => {
      message.style.opacity = "0";
      message.style.transition = "opacity .3s ease";
      window.setTimeout(() => message.remove(), 300);
    }, 3500);
  });
});
