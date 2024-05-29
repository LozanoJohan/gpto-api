from fastapi import FastAPI
from frontend.db import execute_query, conn
from frontend.firebase import upload_chat_message
from frontend.gpt import think_steps
from frontend.sql_coder import generate_query
import config
import dotenv
import os

dotenv.load_dotenv()

app = FastAPI()

@app.get("/get_answer/")
async def get_answer(prompt: str):
    if os.getenv("THINK_PROMPT") == 1:
        print("Think prompt:", os.getenv("THINK_PROMPT"))
        prompt = think_steps(prompt)
    print("Steps:", prompt)
    try:
        data, query = query_database(prompt)  
        try:
            upload_chat_message(prompt, data)
        except Exception as e:
            print("Error al subir mensaje a firebase:", str(e))

        return {"data": data}

    except Exception as e:
        return {"data": e}

def query_database(prompt):
    error = True
    tries = 0

    cursor = conn.cursor()

    while error and tries < config.MAX_TRIES:
        tries += 1
        print(f"Trie: {tries}")

        try:
            query = generate_query(prompt, mssql=True)
            print("Prompt:", prompt)
            print("Query: ", query)
            data = execute_query(query, cursor)
            error = False


        except Exception as e:
            print("Error: ", e)

    if error == True:
        return
    
    return data, query
