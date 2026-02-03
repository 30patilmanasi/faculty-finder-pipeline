import sqlite3
from transform import transform_data

def save_to_db(data):
    """
    Storage: Persists cleaned data in SQLite including newly extracted fields.
    """
    # Create connection to the relational DB
    conn = sqlite3.connect('faculty_data.db')
    cursor = conn.cursor()
    
    # 1. UPDATED SCHEMA: Added teaching, publications, and research columns
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
            teaching TEXT,       -- New Column
            publications TEXT,   -- New Column
            research TEXT,       -- New Column
            profile_url TEXT UNIQUE
        )
    ''')

    # Efficient SQL storage
    for entry in data:
        # 2. UPDATED INSERT: Added the 3 new fields to the query
        cursor.execute('''
            INSERT OR IGNORE INTO faculty (
                name, education, email, phone, address, 
                biography, specialization, teaching, 
                publications, research, profile_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            # 3. UPDATED MAPPING: Passing the new fields from the dictionary
            entry.get('name'), 
            entry.get('education'), 
            entry.get('email'),
            entry.get('phone'), 
            entry.get('address'), 
            entry.get('biography'),
            entry.get('specialization'), 
            entry.get('teaching'),     # New Field
            entry.get('publications'), # New Field
            entry.get('research'),     # New Field
            entry.get('profile_url')
        ))

    conn.commit()
    conn.close()
    print("Clean dataset with academic details saved to faculty_data.db successfully.")

if __name__ == "__main__":
    # Run the modular pipeline
    cleaned_data = transform_data()
    if cleaned_data:
        save_to_db(cleaned_data)