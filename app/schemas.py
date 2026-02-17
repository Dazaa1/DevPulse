from pydantic import BaseModel, Field
from typing import List

class Article(BaseModel):
    title: str = Field(min_length=5)
    content: str
    tags: List[str]

class ArticleResponse(Article):
    id: int
    read_time_minues: int
