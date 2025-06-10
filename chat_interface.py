import streamlit as st
import sqlite3
from llm_sql_translator import get_sql_from_nl

# Function to execute SQL on the database and return results
def run_sql_query(db_path, sql_query):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            col_names = [description[0] for description in cursor.description]
            return col_names, rows
    except Exception as e:
        return [], [[f"Error: {e}"]]

# Streamlit interface
st.set_page_config(page_title="LLM SQL Assistant", layout="wide")
st.title("🔍 LLM-Powered Natural Language to SQL Assistant")

nl_query = st.text_input("Enter your question about the student database:")

if nl_query:
    st.write("🔄 Translating to SQL...")
    sql_query = get_sql_from_nl(nl_query)

    if sql_query:
        st.code(sql_query, language="sql")
        st.write("📊 Executing on database...")

        col_names, result = run_sql_query("student.db", sql_query)

        if col_names:
            st.dataframe([dict(zip(col_names, row)) for row in result])
        else:
            st.write(result[0][0])  # Display error message if any
