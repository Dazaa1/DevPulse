from fastapi import FastAPI
from schemas import Article

# init fastapi
app = FastAPI()

articles = []

@app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

@app.post('/submit')
def submit_article(article: Article):
    articles.append({"title": article.title, "content": article.content, "tages": article.tags})
    return {"ok": "submitted"}

@app.get('/articles')
def retrieve_articles():
    return articles