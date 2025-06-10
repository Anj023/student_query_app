import requests
import re
import json

def get_sql_from_nl(nl_query):
    url = "http://172.25.60.20:11434/api/generate"
    headers = {"Content-Type": "application/json"}

    # Add actual schema so LLM doesn't hallucinate
    schema = """
    You are given a SQLite database with the following table:

    Table: student
    Columns:
    - Name
    - CGPA
    - Location
    - Email
    - Phone Number
    - Preferred Work Location
    - Specialization in degree

    Based on this, write a valid SQL query that answers the question below.
    Only return the SQL query. No explanations. End it with a semicolon (;).
    """

    prompt = f"{schema}\nQuestion: {nl_query}"

    payload = {
    "model": "MFDoom/deepseek-r1-tool-calling:7b",
    "messages": [
        {"role": "system", "content": (
            "You are a SQL generator. You must ONLY respond with a valid SQLite SQL query. "
            "DO NOT include any explanation or commentary. "
            "The database contains a table named 'student' with the following columns:\n"
            "- Name\n- CGPA\n- Location\n- Email\n- Phone Number\n- Preferred Work Location\n- Specialization in degree\n"
        )},
        {"role": "user", "content": nl_query}
    ]
}


    try:
        response = requests.post(url, json=payload, headers=headers)
        print("\nRaw response:")
        print(response.text)

        lines = response.text.strip().splitlines()
        full_response = ""
        for line in lines:
            json_obj = json.loads(line)
            full_response += json_obj.get("response", "")

        # Extract SQL query
        match = re.search(r"(?i)(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER|WITH)[\s\S]+?;", full_response.strip())
        if match:
            return match.group(0).strip()
        else:
            for line in full_response.splitlines():
                line = line.strip()
                if (
                    any(line.upper().startswith(kw) for kw in ["SELECT", "INSERT", "UPDATE", "DELETE"])
                    and ";" in line and not line.endswith(".")
                ):
                    return line
            return "SELECT * FROM student;"  # Fallback

    except Exception as e:
        print("Error parsing LLM response:", e)
        return "SELECT * FROM student;"  # Fallback
