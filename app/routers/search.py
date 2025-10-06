from fastapi import APIRouter

from app.services.search_service import search_articles

router = APIRouter(prefix="/search", tags=["search"])

@router.get('/')
async def search(q: str):
    """
    Endpoint to search articles
    """
    results = search_articles(q,10) # 10 is the limit of articles
    return {"query": q, "results": results}

