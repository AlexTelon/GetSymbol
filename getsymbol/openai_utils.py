import os
import pathlib

import openai

if 'OPENAI_API_KEY' in os.environ:
    openai.api_key = os.environ['OPENAI_API_KEY']
else:
    main_folder = pathlib.Path(__file__).resolve().parent.parent
    api_key_path = main_folder / '.openai_key.secret'
    with open(api_key_path, 'r') as f:
        openai.api_key = f.read().strip()


PROMPT_HEADER = """You are a cli tool that given an input you answer with matching utf chars only.
No text or explanations are allowed. Only unicode symbols. No english words or letters in your response.
Respond with one or more symbols seperated by space only.
"""

def get_symbols(prompt: str) -> str:
    """Given a prompt, return matching symbols."""
    # engine = "text-davinci-003" # works well but most expensive
    engine = 'text-davinci-003' # also seems to work well and might be cheaper?
    # the other engines were bad at least with this current prompt and temperature etc.

    response = openai.Completion.create(
        engine=engine,
        prompt=f"{PROMPT_HEADER}\nInput:{prompt}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=1,
    )

    return response.choices[0].text.strip()

def get_symbol(prompt: str) -> str:
    """Given a prompt, return one matching symbol."""
    engine = 'text-davinci-003'

    response = openai.Completion.create(
        engine=engine,
        prompt=f"{PROMPT_HEADER}.Only return one symbol.\nInput:{prompt}",
        max_tokens=40,
        n=1,
        stop=None,
        top_p=0.01,
    )

    return response.choices[0].text.strip()