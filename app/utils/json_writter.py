import json
from app.utils.base_dir import BASE_DIR

def error_writter(url:str):
    path = BASE_DIR/'data'/'processed'/'noJsonFiles.json'

    with open(path, 'r') as f:
        data:list = json.load(f)
    data.append(url)

    with open(path, 'w') as f:
        json.dump(data, f)

def data_json_writter(processed_data: list):
    path = BASE_DIR/'data'/'processed'/'processedData.json'
    with open(path, 'w') as f:
        json.dump(processed_data, f)
