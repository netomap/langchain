from google import genai
from vars import gemini_api

client = genai.Client(api_key=gemini_api)

for m in client.models.list():
    print (m.name)