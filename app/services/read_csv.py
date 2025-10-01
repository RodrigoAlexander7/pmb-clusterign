import pandas as pd
from app.utils.base_dir import BASE_DIR

def get_data_from_csv():
    df = pd.read_csv(BASE_DIR/'data'/'raw'/'SB_publication_PMC.csv')
    title_url_dict = {}
    for row in df.itertuples():
        title_url_dict[row.Title] = row.Link
    return title_url_dict

