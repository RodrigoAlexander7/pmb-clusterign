from app.utils.base_dir import BASE_DIR
import json

path = BASE_DIR/'data'/'processed'/'clusters.json' 

def get_cluster_json():
    data = []
    with open(path, 'r') as f:
        data = json.load(f)
    return data

b_kwr_path = BASE_DIR/'data'/'processed'/'bigramKeywords.json' 
u_kwr_path = BASE_DIR/'data'/'processed'/'unigramKeywordsKeyBERT.json' 

def get_bigrams_clusters_labeled_json():
    num_kwr = {}    #dict with the number of cluster and the keywords list asociate
    with open(u_kwr_path, 'r') as f:
        num_kwr = json.load(f)
    return num_kwr
    
    

    
    
    





