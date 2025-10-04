from fastapi import APIRouter
from app.services.clustering import get_cluster_json

router = APIRouter(prefix="/cluster", tags=["cluster"])

@router.get('/')
async def getClusters():
    return get_cluster_json()
