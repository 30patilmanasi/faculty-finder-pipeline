#  Faculty Data ETL Pipeline & API Serving

**Course:**  Big Data 
**Academic Year:** 2025-26  


## 📌 Objective
This project demonstrates a complete **Data Engineering Lifecycle**. The objective is to extract data using the **Scrapy** framework, transform it for cleanliness, store it in a structured relational database, and serve it through a modern API layer.


## 🏗 Project Architecture & Lifecycle
#Ingestion: Uses the Scrapy framework to crawl a faculty directory and export raw HTML into a faculty_data.json file.

#Transformation: Employs transform.py to clean raw data and resolve the "null challenge" by labeling missing biographies as "Data is not available".

#Storage: Utilizes store.py and SQLite3 to migrate cleaned data into a structured relational database (faculty_data.db) for persistent storage.

#Serving: Leverages FastAPI and Uvicorn in main.py to provide a RESTful API endpoint (/all), allowing users to consume the final dataset as JSON.

## ⚙️ Prerequisites & 🛠 Technical Stack 
Web Scraping: Scrapy (Asynchronous crawling)
Data Processing: Python Standard Library / Pandas
Database: SQLite3 (Relational Storage)
API Framework: FastAPI (High-performance ASGI)
Server: Uvicorn
---

###  Create a Virtual Environment
It is recommended to use a virtual environment to isolate project dependencies.

**On Windows:**
```bash
python -m venv venv
```
```bash
.\venv\Scripts\Activate.ps1
```
**On Linux (Ubuntu) / macOS:**
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

## ⚙️ How to Run the Project
##1. Activate Environment:  python -m venv venv (\venv\Scripts\activate)
2.Install Dependencies:  pip install fastapi uvicorn scrapy
3.Ingestion (Scraping):  scrapy crawl daiict -o faculty_data.json
4.Storage & Transformation :   python store.py
5.Serving:  python main.py
6.View Data: Open your browser and navigate to: http://127.0.0.1:8000/all

## API Documentation
Once the server is running, you can access the following endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Root endpoint showing API status |
| `/faculty/all` | `GET` | Returns all faculty members in the database. |
| `/docs` | `GET` | Interactive Swagger UI for testing. |


## Project Structure
├── faculty_scraper/          # Scrapy project root directory
│   ├── spiders/              # Crawler directory
│   │   ├── __init__.py       # Package initialization
│   │   └── daiict.py         # Core web scraping logic for faculty profiles
│   ├── __init__.py           # Package initialization
│   ├── items.py              # Scraped data containers/models
│   ├── middlewares.py        # Request and response processing layers
│   ├── pipelines.py          # Default (empty) Scrapy pipelines
│   └── settings.py           # Scrapy project configurations
├── logs/                     # Audit and compliance logs
│   └── llm_usage.md          # AI interaction records (Project Policy requirement)
├── venv/                     # Python Virtual Environment for dependency isolation
├── faculty_data.json         # Raw extracted data (Ingestion Output)
├── faculty_data.csv          # Cleaned dataset in CSV format
├── faculty_data.db           # Structured Relational Database (SQLite)
├── transform.py              # Data cleaning: Removes HTML noise and handles nulls
├── store.py                  # Storage layer: Migrates cleaned data to SQLite
├── main.py                   # FastAPI: Serves processed data via /all endpoint
├── requirements.txt          # Project dependencies (Scrapy, FastAPI, Uvicorn)
├── scrapy.cfg                # Scrapy deployment configuration
└── README.md                 # Project documentation and setup guide
Note: Although the project includes a default pipelines.py file, the Transformation and Storage stages are implemented as separate standalone scripts (transform.py and store.py). This allows for independent debugging of the cleaning logic and database migration without re-running the entire crawl.

📊 Dataset Statistics
The ETL pipeline successfully extracted and processed data for the entire faculty directory.

Category                   Approximate Count

Total Faculty Records          ~110+

Data Points per Record        11 Fields

Total Data Entities           ~1,200+

Database Size                 ~150 KB (SQLite)





**Example Response (`/faculty/all`):**
```json
[
  {
    "id": 1,
    "faculty_type": "Faculty",
    "name": "Yash Vasavada",
    "email": "yash_vasavada@dau.ac.in",
    "phone": "079-68261634",
    "professional_link": "https://www.daiict.ac.in/faculty/yash-vasavada",
    "address": "# 1224, FB-1, DA-IICT, Gandhinagar, Gujarat, India – 382007",
    "qualification": "PhD (Electrical Engineering), Virginia Polytechnic Institute and State University, USA",
    "specialization": "Communication, Signal Processing, Machine Learning, Meet Prof. Yash Vasavada:, A Passionate Researcher in Wireless Communications and Signal Processing",
    "teaching": "Introduction to Communication Systems, Advanced Digital Communications, Next Generation Communication Systems",
    "research": "Research not provided",
    "publications": "Yash Vasavada, , Michael Parr, Nidhi Sindhav, and Saumi S., A Space-Frequency Processor for Identifying and Isolating GNSS Signals Amidst Interference,...",
    "biography": "Yash Vasavada is currently a Professor at DAIICT, and he works in the areas of communication system design and development and application of machine learning algorithms..."
  }
]


## Database Schema

The table below defines the schema for the `Faculty` database and describes the specific transformation logic used to clean "HTML noise" and standardize the data for the API.

| Field | SQLite Type | Description | Cleaning & Transformation Logic |
| :--- | :--- | :--- | :--- |
| **id** | INTEGER | Primary key with auto-increment. | Unique identifier assigned by SQLite upon record insertion. |
| **faculty_type** | TEXT | Classification of the faculty member. | Extracted from the source listing URL and standardized to Title Case. |
| **name** | TEXT | Full name of the faculty member. | Converted to Title Case (e.g., "YASH VASAVADA" to "Yash Vasavada"). |
| **email** | TEXT | Professional email address(es). | Flattened from raw list fragments into a comma-separated string. |
| **phone** | TEXT | Official contact number(s). | Flattened into a unified string; whitespace normalized. |
| **professional_link** | TEXT | Source URL to the individual profile. | Captured as a direct reference to the origin data. |
| **address** | TEXT | Official campus or office address. | Normalized whitespace and stripped leading/trailing commas to remove **HTML noise**. |
| **qualification** | TEXT | Educational background and degrees. | Joined list fragments with a " &#124; " pipe delimiter for readability. |
| **specialization** | TEXT | Areas of professional expertise. | Cleaned of leading/trailing commas and **HTML noise**; joined into a clean string. |
| **teaching** | TEXT | List of courses taught. | Newline-separated for proper display in the API response. |
| **research** | TEXT | Current research interests/projects. | Populated with **"Research not provided"** fallback if source data is missing. |
| **publications** | TEXT | Academic citations and papers. | Intensive cleaning to collapse whitespace and remove **HTML noise/fragments**. |
| **biography** | TEXT | Professional summary/biography. | Joined multiple paragraph fragments into a single continuous block. |



###🏁 Conclusion & Learning Outcomes:
This project successfully implemented a modular Faculty Data ETL Pipeline, demonstrating mastery over the four pillars of data engineering: Ingestion, Transformation, Storage, and Serving. By resolving the "null challenge," I learned to ensure data quality through sanitization logic while building a decoupled system architecture that is scalable and easy to maintain. Furthermore, navigating environment-specific challenges strengthened my skills in building reproducible software and providing data-as-a-service via FastAPI.

🚀 Future Enhancements :
Cross-Institutional Scalability: Generalize Scrapy logic to support diverse directory structures across multiple universities.
Semantic Search Integration: Implement vector embeddings to enable natural language queries against faculty bios.
Analytical Dashboard: Develop a Streamlit or React interface to visualize faculty research trends and expertise.
Automated Synchronization: Schedule periodic crawls using GitHub Actions or Airflow to detect data changes automatically.