document.addEventListener('DOMContentLoaded', function() {
    // Aggiorna la data all'avvio della pagina
    updateDate();

    // Imposta un intervallo per aggiornare la data ogni minuto (60,000 millisecondi)
    setInterval(updateDate, 60000);
});

function updateDate() {
    // Ottieni l'elemento in cui mostrare la data
    var currentDateElement = document.getElementById('currentDate');

    // Crea un oggetto Data per ottenere la data corrente
    var currentDate = new Date();

    // Formatta la data come stringa leggibile
    var formattedDate = currentDate.toLocaleString();

    // Aggiorna il contenuto dell'elemento con la data formattata
    currentDateElement.textContent = 'Data: ' + formattedDate;
}
