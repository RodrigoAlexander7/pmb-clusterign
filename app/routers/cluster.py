from fastapi import APIRouter
from app.services.clustering import get_cluster_json
from app.services.clustering import get_bigrams_clusters_labeled_json

router = APIRouter(prefix="/cluster", tags=["cluster"])

@router.get('/docs')
async def getClusters():
    return get_cluster_json()

@router.get('/bigramKeywords')
async def getKeywordsBigram():
    return get_bigrams_clusters_labeled_json()
