import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    model="gpt4-1106-preview"
)
    return response.choices[0].text.strip()

def get_json_response(system_prompt, user_prompt):
    instruction = "Make sure to return the output in JSON format, where the key would be 'allergy' and the value would be the allergen."
    system_prompt_with_instruction = f"{system_prompt} {instruction}"
    response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    model="gpt4-1106-preview",
    response_format={ "type": "json_object" }
)
    return response.choices[0].text.strip()
