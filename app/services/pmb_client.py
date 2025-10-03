import httpx
from app.utils.json_writter import error_writter
#import asyncio

def get_Url(url: str):
    return url.split('/')[-2]

async def get_content_json(url:str):
    id = get_Url(url)
    new_url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{id}/ascii"
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(new_url)

    # validate the succes status
    if response.status_code != 200:
        return {"error": f"Request failed with status {response.status_code}"}

    #print(response.json()) 
    try:
        print(f"ok ${id}")
        return response.json()
    except Exception:
        print("Invalid JSON response:" , {new_url})
        error_writter(url)
        return 

# a = asyncio.run(get_content_json("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136787/")) 
