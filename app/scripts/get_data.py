from app.services.read_csv import get_data_from_csv
from app.services.preprocessing import preprocessing
from app.utils.json_writter import data_json_writter
import asyncio

async def get_documents_words():
    response = [] # the response is a list with dicts like "title"->["word", "other"]
    title_url_dict = get_data_from_csv()
    for title, url in title_url_dict.items():
        word_str = await preprocessing(url)
        if word_str:
            response.append({title: word_str})
    data_json_writter(response)
    return response

asyncio.run(get_documents_words())
print("succes")
