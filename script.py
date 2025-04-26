import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = "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" # ← your actual API key here


headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "mistralai/mistral-7b-instruct:free",
    "messages": [{"role": "user", "content": "Suggest a birthday gift for a 10-year-old who loves drawing"}],
    "temperature": 0.7
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
