from fastapi import FastAPI
from schemas import Article

articles = []

# init fastapi
app = FastAPI()

@app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

@app.post('/submit')
def submit_article(article: Article):
    articles.append({"title": article.title, "content": article.content, "tags": article.tags})
    return {"article": "submited"}


@app.get('/articles')
def get_articles():
    return articles