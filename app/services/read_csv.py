import pandas as pd
from app.utils.base_dir import BASE_DIR

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
    return url_title_dict
