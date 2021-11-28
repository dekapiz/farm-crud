from fastapi import FastAPI
from routes.penerimaan import penerimaan_router

app = FastAPI()

app.include_router(penerimaan_router)