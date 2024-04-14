import sqlite3

# Function to create and populate the poems table
def setup_database():
    # Connect to SQLite database
    conn = sqlite3.connect('poems.db')
    c = conn.cursor()

    # Create poems table
    c.execute('''CREATE TABLE IF NOT EXISTS poems (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    text TEXT
                )''')

    # Insert data into poems table
    poems_data = [
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
        ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
        ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
        ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
        ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
    ]

    c.executemany('INSERT INTO poems (title, author, text) VALUES (?, ?, ?)', poems_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Call the setup_database function to create and populate the database
setup_database()
