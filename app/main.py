from fastapi import FastAPI
from app.routers import process_data

app = FastAPI()

app.include_router(process_data.router)