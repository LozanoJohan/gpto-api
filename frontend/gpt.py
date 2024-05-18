from openai import OpenAI
from frontend.prompt import MSSQL_TRANSLATOR, DECIDE_FUNCTION, ANSWER_WITH_DATA, THINK_STEPS
import os
from dotenv import load_dotenv

load_dotenv()

openai = OpenAI(
  organization= os.getenv("OPENAI_ORG_ID"),
  api_key= os.getenv("OPENAI_API_KEY")
)

def answer(system_message, prompt, model="gpt-4o", temperature=0, max_tokens=500) -> str:

    messages = [
        {'role': 'system', 'content': system_message},
        {'role': 'user', 'content': prompt}
    ]

    completion = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    # TODO: Mirar para que no consulte si ya lo ha consultado antes

    return completion.choices[0].message.content

def answer_with_data(prompt, data, query):
    return answer(ANSWER_WITH_DATA.format(data=data, query=query), prompt)

def query_translator(query):
    return answer(MSSQL_TRANSLATOR, query, "gpt-3.5-turbo")

def proccess_input(prompt):
    return answer(DECIDE_FUNCTION, prompt)

def think_steps(prompt):
    return answer(THINK_STEPS, prompt)