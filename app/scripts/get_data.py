from app.services.read_csv import get_data_from_csv
from app.services.preprocessing import preprocessing
import asyncio

async def get_documents_words():
    response = [] # the response is a list with dicts like "title"->["word", "other"]
    title_url_dict = get_data_from_csv()
    for i, (title, url) in enumerate(title_url_dict.items()):
        # if i % 45 == 0: # sleep every 45 files otherwise the request can be blocked
        #     await asyncio.sleep(5)
        word_list = await preprocessing(url)
        response.append({title: word_list})
    return response

asyncio.run(get_documents_words())
print("succes")




