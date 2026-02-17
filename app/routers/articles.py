from fastapi import FastAPI, Query, APIRouter
from app.schemas import Article

router = APIRouter()

articles = []

@router.post('/')
def submit_article(article: Article):
    articles.append({"title": article.title, "content": article.content, "tags": article.tags})
    return {"ok": "submitted"}

@router.get('/')
def retrieve_articles(tags: list[str] = Query(None)):
    print(articles)
    if tags:
        for article in articles:
            for tag in tags:
                if tag in article["tags"]:
                    return article
    return articles