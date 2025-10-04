import requests
import json
import ast

class ThemesRecommender:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def recommend(self, text: str):
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        """You are an assistant that gives recommendations of scientific and technical keywords based on one or more input keywords.
                        The output will be used for searching similarities on academic papers and needs to be in English.
                        The output keywords must be diferent from the input keywords.
                        Automatically correct spelling mistakes or variants of scientific terms.
                        If the input is empty, return an empty list.
                        Return exactly a Python list with a maximum of 5 keywords, in lowercase, without accents or punctuation.
                        Do not analyze the question, do not add explanations, just extract the keywords."""
                    )
                },
                {
                    "role": "user",
                    "content": f"Texto:\n'{text}'"
                }
            ],
        }

        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        response.raise_for_status()
        content = response.json()['choices'][0]['message']['content']

        try:
            keywords = ast.literal_eval(content)
            if isinstance(keywords, list):
                return keywords[:5]    # return an array of 5 keywords
        except:
            return content.split(",")  # fallback simple