from fastapi import APIRouter
from app.services.read_csv import get_data_from_csv
from app.services.preprocessing import preprocessing

router = APIRouter(prefix="/data", tags=["data"])

@router.get("/")
async def get_documents_words():
    response = [] # the response is a list with dicts like "title"->["word", "other"]
    title_url_dict = get_data_from_csv()
    for title, url in title_url_dict.items():
        word_list = await preprocessing(url)
        response.append({title: word_list})
    return response



