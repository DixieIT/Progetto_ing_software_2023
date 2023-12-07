# Progetto di Ingegneria del Software 2023 - Sistema di Telemedicina

### Paziente.py
- crea una classe "Paziente" con attributi: "CodiceFiscale", "DataDiNascita", "Nome", "Cognome", "Username", "Password" e "Medico"
- crea i metodi 'getter' e 'setter' per gli attributi del paziente
- crea il metodo "prenota_appuntamento" : per prenotare un appuntamento conoscendo "data" e "motivo"
- crea il metodo "visualizza_anagrafica" : per visualizzare l'anagrafica del paziente
- definisce il metodo __str__ per stampare a video gli attributi del paziente

### create_tables.py
- crea un database 'Pazienti.db', e vi si connette
- crea una tabella "Pazienti" con attributi: "CodiceFiscale", "DataDiNascita", "Nome", "Cognome", "Username", "Password" e "Medico"
- definisce "CodiceFiscale" e "DataDiNascita" come chiave primaria composta
- salva le modifiche e chiude la connessione

### app.py
- configura l'app Flask
- specifica l'indirizzo del database a cui collegarsi
- definisce la classe "Paziente" con : "CodiceFiscale", "DataDiNascita", "Nome", "Cognome", "Username", "Password" e "Medico"
- definisce la route principale
- in caso di richiesta POST:
  - estrae dal'informazione ricevuta i campi : "CodiceFiscale", "DataDiNascita", "Nome", "Cognome", "Username", "Password" e "Medico"
  - passa i campi al costruttore della classe "Paziente" creando un nuovo oggetto di tipo "Paziente"
  - Aggiunge l'oggetto creato al database
  - Salva le modifiche
