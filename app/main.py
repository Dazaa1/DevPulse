from fastapi import FastAPI

# init fastapi
app = FastAPI()

app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

