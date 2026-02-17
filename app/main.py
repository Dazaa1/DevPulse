from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers.articles import router
from sqlmodel import Session

# init fastapi
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

app.include_router(router, prefix='/articles')