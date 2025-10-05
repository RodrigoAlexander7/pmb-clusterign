from app.utils.base_dir import BASE_DIR
from app.services.read_csv import get_url_title_from_csv_json
import json

path = BASE_DIR/'data'/'processed' 
references_path = BASE_DIR/'data'/'processed'/'references.json' 
clusters_path = BASE_DIR/'data'/'processed'/'clusters.json' 
keywords_per_doc_path = BASE_DIR/'data'/'processed'/'keywordsPerDoc.json' 
metadata_path = BASE_DIR/'data'/'processed'/'metadata.json' 

url_title_dict = get_url_title_from_csv_json()

def get_title_by_id(id:str):
    return url_title_dict[id]

def get_id_by_title(title:str):
    for key, value in url_title_dict.items():
        if title in value:
            return key

def get_ref_by_id(id: str):
    ref_dict = {}   # is a dict with {PMB1235 : [ref 01, ref02]}
    with open(references_path, 'r') as f:
        ref_dict = json.load(f)
    return ref_dict[id]

def get_cluster_number(id:str):
    title = get_title_by_id(id)
    clusters_dict = {}
    with open(clusters_path, 'r') as f:
        clusters_dict = json.load(f)
    for key, val in clusters_dict.items():
        if title in val:
            return key


def getKeywordsById(id:str):
    title = get_title_by_id(id)
    keywords_per_doc_dict = {}
    with open(keywords_per_doc_path, 'r') as d:
        keywords_per_doc_dict = json.load(d)
    return keywords_per_doc_dict[title]

def get_metadata(id:str):
    metadata_dict = {}
    with open(metadata_path, 'r') as f:
        metadata_dict = json.load(f)
    return metadata_dict[id]
