import pandas as pd
from app.utils.base_dir import BASE_DIR
import json

def get_Url(url: str):
    return url.split('/')[-2]

def get_data_from_csv():
    df = pd.read_csv(BASE_DIR/'data'/'raw'/'SB_publication_PMC.csv')
    title_url_dict = {}
    for row in df.itertuples():
        title_url_dict[row.Title] = row.Link
    return title_url_dict

def get_url_title_from_csv():
    df = pd.read_csv(BASE_DIR/'data'/'raw'/'SB_publication_PMC.csv')
    url_title_dict = {}
    for row in df.itertuples():
        url_title_dict[get_Url(str(row.Link))] = row.Title
    with open(BASE_DIR/'data'/'processed'/'url_title.json', 'w') as f:
        json.dump(url_title_dict, f)
    return url_title_dict

def get_url_title_from_csv_json():
    res = {}
    with open(BASE_DIR/'data'/'processed'/'url_title.json', 'r') as f:
        res = json.load(f)
    return res