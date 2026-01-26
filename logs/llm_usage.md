Tool Used: Gemini & ChatGPT
Policy Compliance: Every prompt and response used to build this pipeline is logged below.


Interaction 1: Project Initialization

Tool: Gemini
Prompt: "I am starting a project to crawl college faculty data. How do I initialize a Scrapy project named faculty_scraper and set up a Python virtual environment in Windows?"
Response: Provided instructions to use python -m venv venv for isolation and .\venv\Scripts\activate for activation. Recommended scrapy startproject faculty_scraper to generate the standard directory structure.


Interaction 2 : Implementation of Web Scraping Logic

Tool: Chatgpt
Prompt: "How do I implement the scraping logic in daiict.py to navigate a faculty directory, handle pagination, and extract raw HTML into a JSON file?"
Response  The LLM outlined a Scrapy-based ingestion strategy by defining a Spider class with targeted start_urls. It implemented CSS selector logic to navigate pagination and used the parse method to extract specific HTML entities from faculty profiles. Finally, it provided the command-line instructions to export the raw data into a structured faculty_data.json file for further processing.


Interaction 3: Scrapy Engine Lifecycle

Tool: Gemini
Prompt: "How does Scrapy know which function to execute once and which function to execute multiple times during the crawl lifecycle?"
Response: Explained the concept of "Reserved Method Names" (like start_requests and parse) and Scrapy's event-driven architecture, which triggers these methods at defined stages of the crawl.


Interaction 4: Handling the "Null Challenge"

Tool: Gemini
Prompt: "Write a transform.py script to clean HTML noise from the scraped JSON. If a faculty member has a missing biography, how do I set a default value?"
Response: Provided a Python cleaning script using list comprehensions. Recommended a fallback check: bio if bio else "Data is not available" to ensure no null values reach the database.


Interaction 5: Relational Database Storage

Tool: Chatgpt
Prompt: "I need to store faculty data in sqlite3. Design a schema with columns for name, designation, email, biography, and specialization. Write a store.py script to load the data."
Response: Provided a SQL CREATE TABLE statement and a Python script using the sqlite3 library to iterate through the cleaned JSON and insert records while preventing duplicates.


Interaction 6: API Serving with FastAPI

Tool: Gemini
Prompt: "Build a FastAPI serving layer in main.py that connects to faculty_data.db and provides a /all route to return all data as JSON."
Response: Provided code for a FastAPI app that uses a database connection helper to fetch rows, converts them to a list of dictionaries, and returns them via a GET request.

Interaction 7: Data Dictionary Documentation

Tool: Gemini
Prompt: "Help me write a Data Dictionary for my README that explains how I cleaned 'HTML noise' and whitespace from the faculty biographies."
Response: Generated a Markdown table describing each field, its SQLite type, and the specific cleaning logic (like stripping tags and normalizing whitespace) applied during transformation.

