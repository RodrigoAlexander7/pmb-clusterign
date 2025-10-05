from app.utils.base_dir import BASE_DIR
from app.services.read_csv import get_url_title_from_csv_json
import json

path = BASE_DIR/'data'/'processed'/'clusters.json' 

url_title_dict = get_url_title_from_csv_json()

def get_title_by_id(id:str):
    return url_title_dict[id]
