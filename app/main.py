from fastapi import FastAPI, Query
from schemas import Article
from typing import List

# init fastapi
app = FastAPI()

articles = []

@app.get('/checkhealth')
def checkhealth():
    return {"value" : "checkhealth"}

@app.post('/submit')
def submit_article(article: Article):
    articles.append({"title": article.title, "content": article.content, "tags": article.tags})
    return {"ok": "submitted"}

@app.get('/articles/')
def retrieve_articles(tags: List[str] = Query(None)):
    print(articles)
    if tags:
        for article in articles:
            for tag in tags:
                if tag in article["tags"]:
                    return article
    return articles