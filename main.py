from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db_connection():
    # Connects to your persistent relational database
    conn = sqlite3.connect('faculty_data.db')
    # This allows us to access data by column name (e.g., row['name'])
    conn.row_factory = sqlite3.Row  
    return conn

@app.get("/")
def home():
    return {"message": "Welcome to the Faculty API. Use /all to see data."}

@app.get("/all")
def get_all_faculty():
    """
    Serving: Fetches and returns all cleaned faculty data as JSON.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query the 'faculty' table you created and stored data in
    cursor.execute("SELECT * FROM faculty")
    rows = cursor.fetchall()
    
    # Convert relational database rows into a standard JSON list
    data = [dict(row) for row in rows]
    
    conn.close()
    return {"count": len(data), "faculty": data}

if __name__ == "__main__":
    import uvicorn
    # Starts the local development server
    uvicorn.run(app, host="127.0.0.1", port=8000)