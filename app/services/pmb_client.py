import httpx
#import asyncio
from app.utils.url_parse import get_Url

async def get_content_json(url:str):
    id = get_Url(url)
    new_url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{id}/ascii"
    async with httpx.AsyncClient() as client:
        response = await client.get(new_url)
    print(response.json()) 
    return response.json()

# a = asyncio.run(get_content_json("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136787/")) 
