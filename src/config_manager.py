import os
from dotenv import load_dotenv

load_dotenv()

def load_credentials():
    return {'api_key': os.getenv('OPENAI_API_KEY')}


def load_initial_request():
    with open("initial_prompt.txt", 'r', encoding='utf-8') as file:
        initial_prompt = file.read()
    return initial_prompt
