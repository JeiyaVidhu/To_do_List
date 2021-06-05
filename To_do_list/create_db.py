import sqlite3

sql_query = """
    CREATE TABLE IF NOT EXISTS Todo(
         id INTEGER PRIMARY KEY,
         task TEXT,
         complete BOOLEAN);
"""

def execute_query(sql_query):
    with sqlite3.connect('mydb.db') as conn:
        cur = conn.cursor()
        cur.execute(sql_query)
        conn.commit()

if __name__ == '__main__':
    execute_query(sql_query)