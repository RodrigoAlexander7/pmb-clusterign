from fastapi import FastAPI
from app.routers import cluster, data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["GET"],
    allow_headers = ["*"]
)

app.include_router(cluster.router)
app.include_router(data.router)