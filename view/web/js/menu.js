document.addEventListener("DOMContentLoaded", function () {
  const contentDiv = document.querySelector(".active-page");
  const links = document.querySelectorAll(".nav-link");

  function loadPage(page) {
    fetch(`pages/${page}`)
      .then((response) => response.text())
      .then((html) => {
        contentDiv.innerHTML = html;
      })
      .catch((err) => {
        contentDiv.innerHTML = "<p>Erro ao carregar a página.</p>";
        console.error(err);
      });
  }

  // Inicial: carregar página de agendamento
  loadPage("agendamento.html");

  links.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      // Remove classe active de todos os links
      links.forEach((l) => l.classList.remove("active"));
      link.classList.add("active");

      const page = link.getAttribute("data-page");
      if (page) {
        loadPage(page);
      }
    });
  });
});
