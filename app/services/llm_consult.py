import requests
import json

class Consult:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def consult(self, SystemContent: str, UserContent: str):
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (SystemContent)
                },
                {
                    "role": "user",
                    "content": f"Texto:\n'{UserContent}'"
                }
            ],
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()