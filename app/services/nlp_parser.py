import requests
import json
import ast

class KeywordExtractor:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def extract(self, text: str):
        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": (
                        """You are an assistant that extracts only scientific and technical keywords from academic or technical texts.
                        Consider that the output will be used for searching similarities on academic papers.
                        Automatically correct spelling mistakes or variants of scientific terms.
                        The text can be in English or any other language.
                        Ignore generic or common words (such as 'research', 'articles', 'information').
                        First, identify the keywords. After that, convert all terms to their equivalent technical English, not literal translations.
                        If the text does not contain scientific or technical information, return an empty list.
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
                return keywords    # return an array of keywords
        except:
            return content.split(",")  # fallback simple
