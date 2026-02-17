from fastapi import Query, APIRouter, HTTPException
from app.schemas import Article

router = APIRouter()

articles = []

@router.post('/')
def submit_article(article: Article):
    articles.append({"title": article.title, "content": article.content, "tags": article.tags})
    return {"ok": "submitted"}

@router.get('/{article_id}')
def retrieve_articles(article_id: int, tags: list[str] = Query(None)):
    if article_id < 0 or article_id >= len(articles):
        raise HTTPException(status_code=404, detail="Article not found")
    
    article = articles[article_id]

    if tags:
        if not any(tag in article.get("tags", []) for tag in tags):
            raise HTTPException(status_code=404, detail="Article found, but tags do not match")
            
    return article