from openai import OpenAI
from google import genai
import os
import sys

def get_cleaned_prop_text(file):
    try:
        agent = sys.argv[2]
    except:
        agent = 'gemini'

    f = open(file)
    text = f.read()
    prompt = f"Подкорректируй этот текст, исправь несвязности, разбей его на абзацы:\n {text}"
    if agent=='openai':
        openai_key = os.environ.get("OPENAI_API_KEY")
        client = OpenAI(api_key=openai_key)
        res = client.responses.create(
            model='gpt-4o',
            input=prompt
        )
    elif agent=='gemini':
        genai_key = os.environ.get("GENAI_API_KEY")
        client = genai.Client(api_key=genai_key)
        res = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
    else:
       raise ValueError("model could be either 'openai' or 'gemini'")
        
    return res.text

if __name__ == "__main__":
    file = sys.argv[1]
    f = open(f'{file[:-8]}.txt', 'w')
    f.write(get_cleaned_prop_text(file))
    f.close()

