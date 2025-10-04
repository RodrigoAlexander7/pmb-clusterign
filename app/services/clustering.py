from sklearn.feature_extraction.text import TfidfVectorizer
from app.utils.base_dir import BASE_DIR

path = BASE_DIR/'data'/'processed'/'noJsonFiles.json' 

def TF_IDF_vectorizer(text_corpus: list):
    vectorizer = TfidfVectorizer(
        max_features= 10000,  # the max num of words for the total corpus 
        max_df=0.85,    #delete if the word apears on the 85% of docs
        min_df=0.01,    #delete if tye word aperas just on the 1% of docs
    )
    return vectorizer.fit_transform(text_corpus)





