import openai

with open('.openai_key.secret', 'r') as f:
    openai.api_key = f.read().strip()

PROMPT_HEADER = """
You are a cli tool that given an input you answer with matching utf chars only.
No text or explanations are allowed.

input:"""

def get_chars(prompt):
    prompt=f"{PROMPT_HEADER}{prompt}"
    engine = "text-davinci-003" # works well but most expensive
    engine = 'text-davinci-002' # also seems to work well and might be cheaper?
    # the other engines were bad at least with this current prompt and temperature etc.

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=1,
    )

    return response.choices[0].text.strip()