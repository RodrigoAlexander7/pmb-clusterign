from fastapi import APIRouter
from app.services.data import get_title_by_id

router = APIRouter(prefix="/data", tags=["data"])


@router.get('/titleById')
async def getTitleById(id:str):
    get_title_by_id(id)
