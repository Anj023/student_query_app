import pandas as pd
import sqlite3

def ingest_data(excel_file='student.xlsx', db_file='student.db'):
    df = pd.read_excel(excel_file)
    conn = sqlite3.connect(db_file)
    df.to_sql("student", conn, if_exists="replace", index=False)
    conn.close()
if __name__ =="__main__":
    ingest_data()
    print("Data ingestion completed")
