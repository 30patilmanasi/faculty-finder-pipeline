import sqlite3
from transform import transform_data

def save_to_db(data):
    """
    Storage: Persists cleaned data in SQLite.
    """
    # Create connection to the relational DB
    conn = sqlite3.connect('faculty_data.db')
    cursor = conn.cursor()

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
            teaching TEXT,       
            publications TEXT,   
            research TEXT,       
            profile_url TEXT UNIQUE
        )
    ''')

    # Efficient SQL storage
    for entry in data:
        cursor.execute('''
            INSERT OR IGNORE INTO faculty (
                name, education, email, phone, address, 
                biography, specialization, teaching, 
                publications, research, profile_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (

            entry.get('name'), 
            entry.get('education'), 
            entry.get('email'),
            entry.get('phone'), 
            entry.get('address'), 
            entry.get('biography'),
            entry.get('specialization'), 
            entry.get('teaching'),     
            entry.get('publications'), 
            entry.get('research'),     
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