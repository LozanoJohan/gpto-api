import requests
import dotenv
import os

from frontend.prompt import SQL_CODER_PROMPT, database_schema
from frontend.gpt import query_translator

dotenv.load_dotenv()

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/fca95b5a6208f30b8d27a365a86a9139/ai/run/"
headers = {"Authorization": f"Bearer {os.getenv('CLOUDFLARE_API_KEY')}"}


def run(model, inputs):
    input = {"messages": inputs}
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)

    return response.json()["result"]["response"]


def generate_query(question, mssql=False):
    inputs = [
        {
            "role": "system",
            # Encriptar los datos :p
            "content": SQL_CODER_PROMPT.format(
                question=question, database_schema=database_schema
            ),
        },
        {"role": "user", "content": question},
    ]

    mysql_query = run("@cf/defog/sqlcoder-7b-2", inputs)
    print(mysql_query)
    if mssql:
        return query_translator(mysql_query)

    else:
        return mysql_query


if __name__ == "__main__":

    question = "que producto nos ha generado mas ventas"
    generated_sql = generate_query(question)
    print(generated_sql)
