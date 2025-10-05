from app.utils.base_dir import BASE_DIR
from app.services.data import get_id_by_title
import json

path = BASE_DIR/'data'/'processed'/'clusters.json' 

def get_cluster_json():
    data = {}
    res = {}

    with open(path, 'r') as f:
        data = json.load(f)

    for key, title_list in data.items():
        res[key] = []
        for title in title_list:
            res[key].append({title: get_id_by_title(title)}) 

    return res

b_kwr_path = BASE_DIR/'data'/'processed'/'bigramKeywords.json' 
u_kwr_path = BASE_DIR/'data'/'processed'/'unigramKeywordsKeyBERT.json' 

def get_bigram_clusters_labeled_json():
    num_kwr = {}    #dict with the number of cluster and the keywords list asociate
    with open(b_kwr_path, 'r') as f:
        num_kwr = json.load(f)
    return num_kwr
    
def get_unigram_clusters_labeled_json():
    num_kwr = {}    #dict with the number of cluster and the keywords list asociate
    with open(u_kwr_path, 'r') as f:
        num_kwr = json.load(f)
    return num_kwr
    
    

    
    
    





