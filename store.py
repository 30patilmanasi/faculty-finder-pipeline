import sqlite3
from transform import transform_data

def save_to_db(data):
    """
    Storage: Persists cleaned data in SQLite.
    """
    # Create connection to the relational DB
    conn = sqlite3.connect('faculty_data.db')
    cursor = conn.cursor()
    
    # Design the schema with specific columns for extracted entities
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faculty (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            education TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            biography TEXT,
            specialization TEXT,
            profile_url TEXT UNIQUE
        )
    ''')

    # Efficient SQL storage
    for entry in data:
        cursor.execute('''
            INSERT OR IGNORE INTO faculty (
                name, education, email, phone, address, 
                biography, specialization, profile_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            entry['name'], entry['education'], entry['email'],
            entry['phone'], entry['address'], entry['biography'],
            entry['specialization'], entry['profile_url']
        ))

    conn.commit()
    conn.close()
    print("Clean dataset saved to faculty_data.db successfully.")

if __name__ == "__main__":
    # Run the modular pipeline
    cleaned_data = transform_data()
    if cleaned_data:
        save_to_db(cleaned_data)