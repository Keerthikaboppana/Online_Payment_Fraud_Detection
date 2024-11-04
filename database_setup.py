import sqlite3

def initialize_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            aisle TEXT,
            section TEXT,
            x_coord INTEGER,
            y_coord INTEGER
        )
    ''')
    # Example data entry
    cursor.execute('INSERT INTO products (name, aisle, section, x_coord, y_coord) VALUES (?, ?, ?, ?, ?)', 
                   ("Apple", "Aisle 1", "Fruit Section", 50, 100))
    conn.commit()
    conn.close()

initialize_db()
