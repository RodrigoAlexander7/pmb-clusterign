from fastapi import APIRouter

import app.services.data as dt

router = APIRouter(prefix="/data", tags=["data"])


@router.get('/titleById')
async def getTitleById(id:str):
    return dt.get_title_by_id(id)

@router.get('/idByTitle')
async def getIdByTitle(title:str):
    return dt.get_id_by_title(title)

@router.get('/keywordsById')
async def getKeywordsById(id:str):
    return dt.getKeywordsById(id)
    
@router.get('/referencesById')
async def getRefId(id:str):
    return dt.get_ref_by_id(id)
    
@router.get('/clusterNumber')
async def getClusterNum(id:str):
    return dt.get_cluster_number(id)
    
@router.get('/metadataById')
async def getMetadata(id:str):
    return dt.get_metadata(id)
    



