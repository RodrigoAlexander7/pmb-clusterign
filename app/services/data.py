from app.utils.base_dir import BASE_DIR
from app.services.read_csv import get_url_title_from_csv_json
import json

path = BASE_DIR/'data'/'processed' 
references_path = BASE_DIR/'data'/'processed'/'references.json' 

url_title_dict = get_url_title_from_csv_json()

def get_title_by_id(id:str):
    return url_title_dict[id]

def get_ref_by_id(id: str):
    ref_dict = {}   # is a dict with {PMB1235 : [ref 01, ref02]}
    with open(references_path, 'r') as f:
        ref_dict = json.load(f)
    return ref_dict[id]