from app.services.read_csv import get_data_from_csv
from app.services.read_csv import get_url_title_from_csv
from app.services.preprocessing import preprocessing
from app.services.preprocessing import extract_texts
from app.services.pmb_client import get_content_json
from app.utils.json_writter import data_json_writter
from app.utils.json_writter import no_clean_data_json_writter
from app.utils.base_dir import BASE_DIR
import json
from collections import defaultdict

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


def extract_references_from_json(json_data, max_refs=10):
    texts = []
    found_references = False

    if isinstance(json_data, list):
        if not json_data:  # lista vacía
            return texts
        root = json_data[0]
    elif isinstance(json_data, dict):
        root = json_data
    else:
        return texts  
    
    documents = root.get("documents", [])
    if not documents:
        return texts

    passages = documents[0].get("passages", [])
    for passage in passages:
        text = passage.get("text", "")
        if text == "References":
            found_references = True
            continue
        if found_references:
            texts.append(text)
            # Max limit 10
            if len(texts) >= max_refs:
                break

    return texts



async def get_references_by_url(url:str):
    json_data = await get_content_json(url)
    text_list = extract_references_from_json(json_data)
    return text_list # [Pepe et al, How to cut hair by Pepe, etc]

async def writte_references():
    reference_path = BASE_DIR/'data'/'processed'/'references.json'
    url_title_path = BASE_DIR/'data'/'processed'/'url_title.json'
    url_title_dict = {}
    res = defaultdict(list)

    with open(url_title_path, 'r') as f:
        url_title_dict = json.load(f)
    
    for id in url_title_dict.keys():
        url = f'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{id}/ascii'
        references_list:list = await get_references_by_url(url)
        res[id] = references_list
        print('ok')
    
    with open(reference_path, 'w') as d:
        json.dump(res, d)

    
def get_id(url: str):
    return url.split('/')[-2]

asyncio.run(writte_references())







