from google import genai
from google.genai import types


def get_api_key():
    api_key = input("Please enter your api key: ")
    return api_key

api_key = get_api_key()
print(api_key)
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How does AI work?",

)
print(response.text)