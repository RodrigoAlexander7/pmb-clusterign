import spacy

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



