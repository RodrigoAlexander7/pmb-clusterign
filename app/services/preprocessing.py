import spacy
import app.services.pmb_client as pmb_client
from app.utils.stopwords import is_stopword

# extract all the "text" fields on json
def extract_texts(obj): # obj represent a dictionary or an list (cause json format is like that)
    results = ""
    
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "text":
                results += str(v)
            else:
                results+=(extract_texts(v))
    elif isinstance(obj, list):
        for item in obj:
            results+=(extract_texts(item))
    
    return results

# lemmatization children -> child
nlp = spacy.load('en_core_web_sm')
def lematization(text: str):
    doc = nlp(text)
    lemmas = [
        token.lemma_.lower()
        for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return lemmas

"""
    get the json from url
    get just the elements with the 'text' tag in the json
    clear the jeson (stopwords) and lemmatize text
    return title - important words[]
"""
async def preprocessing(url: str):
    preprocessing_strs = set() 
    response_json = await pmb_client.get_content_json(url)
    document_text = extract_texts(response_json)
    lemmas = lematization(document_text)
    for lemma in lemmas:
        if not is_stopword(lemma):
            preprocessing_strs.add(lemma)
    return preprocessing_strs # return a list with useful words per article






