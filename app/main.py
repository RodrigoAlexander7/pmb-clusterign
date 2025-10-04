from fastapi import FastAPI
from app.routers import cluster

app = FastAPI()

app.include_router(cluster.router)