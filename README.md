---
title: Faculty Finder
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
license: mit
short_description: Smart Faculty Discovery Interface
---

#  Faculty Finder: AI-Powered Recommender System

## Author
- **Names:** Manasi Patil & Krishna Prajapati
- **Roll Nos:** 202518034, 202518024
- **Program:** MSc Data Science 
- **Institution:** DAIICT, Gandhinagar
- **Course:** Big Data Systems
- **Academic Year:** 2025-26


## Small Motivation

"Success doesn't come from what you do occasionally, it comes from what you do consistently" 


##  Live Application
**Access the live AI Search Interface here:** 
(https://manasipatil30-faculty-finder.hf.space)        ## Too excess the link (Ctrll+click)


##  Objective
This project demonstrates a complete **Data Engineering Lifecycle**. The objective is to extract data using the **Scrapy** framework, transform it for cleanliness, store it in a structured relational database, and serve it through a modern API layer.

The pipeline is designed to prepare high-quality data that can later support analytical and semantic queries such as:

> “Who is working on sustainable energy and carbon capture?”


##  Project Architecture & Lifecycle

The project follows a modular **ETL (Extract–Transform–Load)** architecture:

###Ingestion: 
- Uses the Scrapy framework to crawl a faculty directory and export raw HTML into a faculty_data.json file.
- Outputs raw data into `faculty_data.json` or `faculty_data.csv`.

###Transformation: 
Employs transform.py to clean raw data and resolve the "null challenge" by labeling missing biographies as "Data is not available".

###Storage: 
Utilizes store.py and SQLite3 to migrate cleaned data into a structured relational database (faculty_data.db) for persistent storage.

###Serving: Leverages FastAPI and Uvicorn in main.py to provide a RESTful API endpoint (/all), allowing users to consume the final dataset as JSON.


##  Prerequisites &  Technical Stack 
Web Scraping: Scrapy (Asynchronous crawling)
Data Processing: Python Standard Library / Pandas
Database: SQLite3 (Relational Storage)
API Framework: FastAPI (High-performance ASGI)
Server: Uvicorn


##  How to Run the Project
##1. Activate Environment:  python -m venv venv (\venv\Scripts\activate)

2.Install Dependencies:  pip install fastapi uvicorn scrapy

3.Ingestion (Scraping):  scrapy crawl daiict -o faculty_data.json

4.Storage :   python store.py

5.Transformation : python transform.py

6.Serving:  python main.py

7.View Data: Open your browser and navigate to: http://127.0.0.1:8000/all


## Installation & Setup

Follow these steps to set up the Faculty Data Engineering Pipeline on your local machine.

### 1. Prerequisites

* **Python 3.10+**
* **curl**: Required for website connectivity checks in the shell script.

  **On Ubuntu:**

  ```bash
  sudo apt update && sudo apt install curl -y
  ```

### 2. Clone the Repository

Open your terminal (PowerShell on Windows, or Bash on Linux/macOS) and run:

```bash
git clone https://github.com/30patilmanasi/faculty-finder-pipeline.git
```

```bash
cd faculty-finder-pipeline
```
### 3. Create a Virtual Environment

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
### 4. Install Required Dependencies

```bash
pip install -r requirements.txt
``` 
### 5 . Running the Data Pipeline python code (Bash)

-scrapy crawl faculty_spider -o raw_data.json       #Ingestion (Scraping):
-python transform.py                                #Transformation (Cleaning):
-python store.py                                    #python store.py(storage)
-python main.py                                     #Serving (API)
-semantic_search.py                                 # Serving (Web Interface)               


## API Documentation 
Once the server is running, you can access the following endpoints:

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Root endpoint showing API status |
| `/faculty/all` | `GET` | Returns all faculty members in the database. |
| `/docs` | `GET` | Interactive Swagger UI for testing. |


 ##  Structure : Steps to deploy your project to Hugging Face Spaces.

Step 1: Create the Space
1. Log in to Hugging Face.
2. Click on your profile icon (top right) and select "New Space".
3. Name your Space: e.g., Faculty-Finder-AI.
4.Select SDK: Choose Streamlit (this is vital for your app.py).
5.Visibility: Set to Public (so your professor can see it).
6. Click "Create Space".


##Step 2: Upload Your Files

1. In your new Space, go to the Files tab.
2. Click "Add file" -> "Upload files".
3.Drag and drop these essential files:
4.app.py (The main search interface)
5.faculty_data.db (The SQLite database with the faculty data)
6.requirements.txt (List of libraries to install)
7.README.md (The report we just finalized)
8.semantic_search.py (The AI logic)


##Step 3: Configure requirements.txt

streamlit
pysqlite3-binary
sentence-transformers
torch
pandas

##Step 5: Final Verification
1. Click the App tab.
2. Wait for the BERT model to download (it takes about 30 seconds the first time).
3. Test the search: Type "Arpit Rana" or "Machine Learning".
4. If the results appear with match scores, your deployment is successful!

##Step 6: Share the Link

1.Look at your browser's address bar.
2.Copy the URL (it should look like "https://manasipatil30-faculty-finder.hf.space".)
3.Optional: To get a clean link, click the "..." (three dots) in the top right of the Space and select "Embed this Space" -> copy the Direct URL.


##  Project Structure

├── faculty_scraper/          # Scrapy project root directory

│   ├── spiders/              # Crawler directory

│   │   ├── __init__.py       # Package initialization

│   │   └── daiict.py         # Core web scraping logic for faculty profiles

│   ├── items.py              # Scraped data containers/models

│   ├── settings.py           # Scrapy project configurations

│   └── ...                   # Other Scrapy internal files

├── logs/                     # Audit and compliance logs

│   └── llm_usage.md          # AI interaction records (Project Policy requirement)

├── venv/                     # Python Virtual Environment for dependency isolation

├── faculty_data.json         # Raw extracted data (Ingestion Output)

├── faculty_data.csv          # Cleaned dataset in CSV format

├── faculty_data.db           # Structured Relational Database (SQLite)

├── transform.py              # Data cleaning: Removes HTML noise and handles nulls

├── store.py                  # Storage layer: Migrates cleaned data to SQLite

├── semantic_search.py        # AI Logic: BERT-based vector search and similarity

├── app.py                    # Streamlit UI: The main web application for users

├── main.py                   # FastAPI: Serves processed data via API endpoints

├── requirements.txt          # Project dependencies (Streamlit, Scrapy, Transformers)

├── .gitignore                # Specified files for Git to ignore (like venv/)

├── scrapy.cfg                # Scrapy deployment configuration

└── README.md                 # Project documentation and setup guide


Note: Although the project includes a default pipelines.py file, the Transformation and Storage stages are implemented as separate standalone scripts (transform.py and store.py). This allows for independent debugging of the cleaning logic and database migration without re-running the entire crawl.


##  Data Transformation Logic

The transformation layer ensures that raw data from the university website is standardized and optimized for the AI search model. The pipeline performs the following steps:

* **Validation:** Verifies the existence of raw JSON input before processing to prevent pipeline failure.
* **Flattening:** Converts complex list-type data (e.g., multiple research interests) into flat strings for easier database indexing.
* **Normalization:** * Removes HTML tags and unwanted noise using regex.
* Standardizes names and faculty titles into **Title Case** (e.g., `ARPIT RANA` → `Arpit Rana`).
* Cleans faculty designations (replaces hyphens with spaces for better readability).
* **Missing Value Handling:** * Assigns placeholder text (e.g., "Information not listed") for content-related fields like `biography` and `teaching` to ensure a consistent UI.
    * Sets technical fields to `null` where appropriate for database integrity.
* **Output:** Generates a production-ready `cleaned_data.json` used for final database insertion.

## Data Storage Logic

The storage stage persists the cleaned faculty data into a relational SQLite database.

- Validates cleaned JSON input.  
- Initializes SQLite database and creates `Faculty` table if missing.  
- Loads cleaned data using batch `INSERT OR IGNORE` for efficiency.  
- Commits all inserts in a single transaction to ensure consistency.   


##  Dataset Statistics

The ETL pipeline successfully extracted and processed data for the entire faculty directory.

Category                   Approximate Count

Total Faculty Records          ~110+

Data Points per Record        11 Fields

Total Data Entities           ~1,200+

Database Size                 ~150 KB (SQLite)

Storage Engine                 SQLite

Lowest Data Density           research (12.6%)

Feild per Record              13

### Field-Level Statistics

| Field Name | Null Count | Density (%) | Avg Words | Avg Characters | Min Characters | Max Characters |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| id | 0 | 100.0 | 1.0 | 2.0 | 1 | 3 |
| faculty_type | 0 | 100.0 | 1.5 | 11.7 | 7 | 29 |
| name | 0 | 100.0 | 2.2 | 14.6 | 7 | 29 |
| email | 0 | 100.0 | 1.1 | 24.4 | 3 | 51 |
| phone | 0 | 100.0 | 1.1 | 10.1 | 3 | 36 |
| professional_link | 0 | 100.0 | 1.0 | 52.1 | 40 | 75 |
| address | 0 | 100.0 | 6.7 | 42.7 | 3 | 138 |
| qualification | 2 | 98.2 | 6.9 | 53.6 | 13 | 138 |
| specialization | 3 | 97.3 | 16.9 | 137.5 | 7 | 2020 |
| teaching | 54 | 51.4 | 21.5 | 172.5 | 33 | 1202 |
| research | 97 | 12.6 | 44.2 | 336.4 | 29 | 1908 |
| publications | 44 | 60.4 | 343.2 | 2574.8 | 75 | 12373 |
| biography | 43 | 61.3 | 126.9 | 860.1 | 184 | 2439 |


### Key Auditing Insights

- Core identity fields (`name`, `email`, `faculty_type`) are fully populated.

- Descriptive academic fields (`teaching`, `research`, `publications`) show expected sparsity due to optional source availability.

- High maximum character counts in `publications` and `biography` indicate rich long-form academic content.

- Overall, the dataset demonstrates strong structural consistency with selective sparsity in deep-profile fields.## Dependencies


## Dependencies

- **Scrapy** – Web scraping and crawling framework for data ingestion.  
- **Pandas** – Data cleaning, transformation, and auditing.  
- **SQLAlchemy / SQLite3** – Local database storage and ORM support.  
- **FastAPI** – High-performance REST API for serving processed data.  
- **Uvicorn** – ASGI server to run the FastAPI application.  
- **Sentence-Transformers** – Semantic text embedding generation for search.  
- **PyTorch (torch)** – Tensor computation and embedding storage backend.  
- **Hugging Face Hub** – Model loading and local transformer cache management.



## Database Schema

The table below defines the schema for the `Faculty` database and describes the specific transformation logic used to clean "HTML noise" and standardize the data for the API.

| Field | SQLite Type | Description | Cleaning & Transformation Logic |

| :--- | :--- | :--- | :--- |
| **id** | INTEGER | Primary key with auto-increment. | Unique identifier assigned by SQLite upon record insertion. |

| **faculty_type** | TEXT | Classification of the faculty member. | Extracted from the source listing URL and standardized to Title 
Case. |

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



### Conclusion & Learning Outcomes:

This project successfully implements a modular Faculty Data ETL Pipeline, demonstrating all four pillars of data engineering:

  - Ingestion

  - Transformation

  - Storage

  - Serving

Key learnings include:

  - Handling unstructured web data

  - Managing missing values systematically

  - Designing reusable and maintainable pipelines

  - Exposing data as a service using FastAPI

Future Enhancements :

Cross-Institutional Scalability: Generalize Scrapy logic to support diverse directory structures across multiple universities.

Semantic Search Integration: Implement vector embeddings to enable natural language queries against faculty bios.

Analytical Dashboard: Develop a Streamlit or React interface to visualize faculty research trends and expertise.

Automated Synchronization: Schedule periodic crawls using GitHub Actions or Airflow to detect data changes automatically.



# DA-IICT Faculty ETL Pipeline 

This project is a fully automated **ETL (Extract, Transform, Load)** pipeline designed to scrape, clean, store, and serve faculty data from the DA-IICT website.



---

## Automation: The One-Command Run
To simplify the project lifecycle, I have developed an **Orchestration Script**. This script manages the sequential execution of the crawler, the data processor, and the web server.

### **Orchestration Script (`run_pipeline.py`)**
This script automates the manual terminal commands into a single execution flow:

```python
import subprocess
import sys

def run_command(command):
    """Utility function to run shell commands"""
    process = subprocess.run(command, shell=True)
    if process.returncode != 0:
        print(f" Error running command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    print(" Starting Faculty Data Pipeline...\n")

    # Step 1: Run Scrapy spider (Extraction)
    print("1️ Running web scraper...")
    run_command("scrapy crawl faculty -o faculty_data.json")

    # Step 2: Run transformation and storage (Transform & Load)
    print("\n2️ Running transformation and storage...")
    run_command("python store.py")

    # Step 3: Start API server (Serve)
    print("\n3️ Starting API server...")
    run_command("python main.py")




**Example Response (`/faculty/all`):**
```json
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
