import httpx
#import asyncio
def get_Url(url: str):
    return url.split('/')[-2]

async def get_content_json(url:str):
    id = get_Url(url)
    new_url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{id}/ascii"
    async with httpx.AsyncClient() as client:
        response = await client.get(new_url)
    print(response.json()) 
    return response.json()

# a = asyncio.run(get_content_json("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4136787/")) 
