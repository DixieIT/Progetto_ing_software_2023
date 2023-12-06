import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create Paziente table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS paziente (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        cognome TEXT NOT NULL,
        data_di_nascita DATE NOT NULL,
        username TEXT,
        password TEXT,
        medico TEXT
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Tables created successfully.")
