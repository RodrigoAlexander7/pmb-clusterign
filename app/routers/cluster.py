from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.services.clustering import get_cluster_json
from app.services.clustering import get_bigram_clusters_labeled_json
from app.services.clustering import get_unigram_clusters_labeled_json

router = APIRouter(prefix="/cluster", tags=["cluster"])

@router.get('/cluster')
async def getClusters():
    return get_cluster_json()

@router.get('/bigramKeywords')
async def getKeywordsBigram():
    return get_bigram_clusters_labeled_json()


@router.get('/unigramKeywords')
async def getKeywordsUnigram():
    data = get_unigram_clusters_labeled_json()
    return JSONResponse(content=data)