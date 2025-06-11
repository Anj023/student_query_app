# LLM-Powered Natural Language to SQL Assistant

This is a Streamlit-based app that allows users to query a student database using natural language. The app translates user questions into SQL queries using an LLM (Large Language Model) hosted via Ollama, runs the queries on a local SQLite database, and displays the results.

---

## Features

- Accepts user questions in plain English (e.g., "Show all students with CGPA above 9")
- Translates questions to SQL queries using a locally hosted LLM (Ollama)
- Runs the SQL queries on a `student.db` SQLite database
- Displays results in a tabular format
- Reads data from an Excel file `student.xlsx` and ingests it into the database

---

## Project Structure
student_query_app/
│
├── chat_interface.py # Streamlit UI for user interaction
├── llm_sql_translator.py # Handles prompt generation and API call to LLM
├── data_ingest.py # Ingests Excel data into SQLite database
├── student.xlsx # Sample data file
└── student.db # Auto-generated database

#Set up your environment 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# install all the dependencies 
pip install openxyl request 

#Run the code 
1. python data_ingest.py # will craete a db 
2. ollama run MFDoom/deepseek-r1-tool-calling:7b
3. streamlit run chat_interface.py #run the app 
