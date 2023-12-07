document.addEventListener("DOMContentLoaded", function () {
  // Crea l'elemento di input per la ricerca
  var searchInput = document.createElement("input");
  searchInput.type = "text";
  searchInput.placeholder = "Cerca su Google...";
  searchInput.id = "search-input";

  // Crea l'elemento del pulsante di ricerca
  var searchButton = document.createElement("button");
  searchButton.innerHTML = "Cerca";
  searchButton.id = "search-button";

  // Aggiungi un listener per la ricerca quando viene premuto il pulsante
  searchButton.addEventListener("click", function () {
    var searchTerm = searchInput.value.trim();
    if (searchTerm !== "") {
      // Redirect a Google con il termine di ricerca
      window.location.href = "https://www.google.com/search?q=" + encodeURIComponent(searchTerm);
    }
  });

  // Aggiungi la barra di ricerca al tuo container
  var searchContainer = document.createElement("div");
  searchContainer.className = "search-container";
  searchContainer.appendChild(searchInput);
  searchContainer.appendChild(searchButton);

  // Aggiungi la barra di ricerca al tuo container HTML
  var container = document.querySelector(".container");
  container.appendChild(searchContainer);
});
