from typing import Annotated
from fastapi import Query, APIRouter, HTTPException, Depends
from ..database import Article
from sqlalchemy.orm import Session
from ..database import engine


router = APIRouter()

articles = []

# ensuring that sessions are closed and opened per request, not sure yet what it means
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@router.post('/')
def submit_article(article: Article, session: Session):
    session.add(article)
    session.commit()
    session.refresh(article)
    return article

@router.get('/{article_id}')
def retrieve_articles(db: Session, article_id: int, tags: list[str] = Query(None)):
    if article_id < 0 or article_id >= len(articles):
        raise HTTPException(status_code=404, detail="Article not found")
    
    article = articles[article_id]

    if tags:
        if not any(tag in article.get("tags", []) for tag in tags):
            raise HTTPException(status_code=404, detail="Article found, but tags do not match")
            
    return db.query(article).all()