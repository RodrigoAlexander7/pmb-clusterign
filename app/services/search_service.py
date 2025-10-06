from whoosh import index
from whoosh.qparser import QueryParser
from app.utils.base_dir import BASE_DIR
import os

# Ruta al índice (ajustar si es necesario)
INDEX_DIR = BASE_DIR/'notebooks'/'indexdir'

def search_articles(query: str, limit: int = 5):
    """Search index with the index"""
    if not os.path.exists(INDEX_DIR):
        return {"error": "The index not exist"}

    ix = index.open_dir(INDEX_DIR)

    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)
        q = parser.parse(query)
        results = searcher.search(q, limit=limit)
        hits = [
            {
                "title": r["title"],
                "score": r.score
            }
            for r in results
        ]
        return hits
