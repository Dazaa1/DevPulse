from fastapi import FastAPI
from app.routers.articles import router

# init fastapi
app = FastAPI()

@app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

app.include_router(router, prefix='/articles')