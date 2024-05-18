import pymssql
from dotenv import load_dotenv
import os

load_dotenv()

def connect(server = None, user = None, database = None, password = None, port = None):
    return pymssql.connect(
        database=database or os.getenv("DATABASE"),
        password=password or os.getenv("PASSWORD"),
        server=server or os.getenv("SERVER"),
        user=user or os.getenv("USERNAME"),
        port=port or os.getenv("PORT"),
        as_dict=True,
    )

conn = connect()

def execute_query(query, cursor):
    """Run SQL query"""
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    conn = connect()

    query = """SELECT TOP 1 c.NOMBRECLIENTE
                FROM CLIENTES c
                JOIN FACTURASVENTA f ON c.CODCLIENTE = f.CODCLIENTE
                ORDER BY f.FECHA DESC;"""

    df = execute_query(query, conn.cursor())
    print(df)
