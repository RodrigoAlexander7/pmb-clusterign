from app.services.read_csv import get_data_from_csv
from app.services.preprocessing import preprocessing
from app.services.preprocessing import extract_texts
from app.services.pmb_client import get_content_json
from app.utils.json_writter import data_json_writter
from app.utils.json_writter import no_clean_data_json_writter

import asyncio

async def get_clean_documents_words():
    response = [] # the response is a list with dicts like "title"->["clean text witout context"]
    title_url_dict = get_data_from_csv()
    for title, url in title_url_dict.items():
        word_str = await preprocessing(url)
        if word_str:
            response.append({title: word_str})
    data_json_writter(response)
    return response

async def get_documents_words():
    response = [] # the response is a list with dicts like "title"->[" this is a context sentence"]
    title_url_dict = get_data_from_csv()
    for title, url in title_url_dict.items():
        doc_json = await get_content_json(url)
        text_str = extract_texts(doc_json)
        if text_str:
            response.append({title: text_str})
    no_clean_data_json_writter(response)
    return response


asyncio.run(get_documents_words())
print("succes")
