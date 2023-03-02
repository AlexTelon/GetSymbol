import openai

# Read the OpenAI API key from a hidden local file
with open('.openai_key.secret', 'r') as f:
    openai.api_key = f.read().strip()

# Input: arrows
# Example output:
# ⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟

# Input: degrees
# Example
# ° ℃ ℉

# Input: letters with dots over them
# Example:
# ̇a ̇b ̇c ḍe ḥf ḳg ḷh ṃi ṇj ṛk ṣl ṭm ̇n ̇o ̇p ̇q ṡr ṭu ṿw ẋx ẏy ̣z
# ̇A ̇B ḌC ḤD ḲE ḶF ṂG ṆH ṚI ṢJ ṬK ̇L ̇M ̇N ̇O ̇P ̇Q ṢR ṬU ṾV ẊW ẎX ẒY


# Define the standard prompt header
PROMPT_HEADER = """
You are a cli tool that given an input you answer with matching utf chars only.
No text or explanations are allowed.

input:"""

def get_chars(prompt):

    prompt=f"{PROMPT_HEADER}{prompt}"
    print(prompt)

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=1,
    )

    # Return the response text as a string
    return response.choices[0].text.strip()