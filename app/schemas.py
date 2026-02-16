from pydantic import BaseModel


class Article(BaseModel):
    title: str
    content: str
    tags: list[str]