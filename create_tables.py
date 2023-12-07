import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('Pazienti.db')
cursor = conn.cursor()

# Create Paziente table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pazienti (
        CodiceFiscale TEXT NOT NULL,
        DataDiNascita TEXT NOT NULL,
        Nome TEXT NOT NULL,
        Cognome TEXT NOT NULL,
        Username TEXT,
        Password TEXT,
        Medico TEXT,
        PRIMARY KEY (CodiceFiscale, DataDiNascita)
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Tables created successfully.")
