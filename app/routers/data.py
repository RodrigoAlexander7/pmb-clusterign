from fastapi import APIRouter
from app.utils.base_dir import BASE_DIR
import json
from app.services.data import get_title_by_id
from app.services.data import get_ref_by_id


router = APIRouter(prefix="/data", tags=["data"])
keywords_per_doc_path = BASE_DIR/'data'/'processed'/'keywordsPerDoc.json' 


@router.get('/titleById')
async def getTitleById(id:str):
    return get_title_by_id(id)

@router.get('/keywordsById')
async def getKeywordsById(id:str):
    title = get_title_by_id(id)
    keywords_per_doc_dict = {}
    with open(keywords_per_doc_path, 'r') as d:
        keywords_per_doc_dict = json.load(d)
    return keywords_per_doc_dict[title]
    
@router.get('/referencesById')
async def getRefId(id:str):
    return get_ref_by_id(id)
    



