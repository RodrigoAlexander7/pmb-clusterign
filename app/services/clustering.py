from app.utils.base_dir import BASE_DIR
import json

path = BASE_DIR/'data'/'processed'/'clusters.json' 

def get_cluster_json():
    data = []
    with open(path, 'r') as f:
        data = json.load(f)
    return data




