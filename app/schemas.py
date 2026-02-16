from pydantic import BaseModel
import uuid
from typing import List


class Article(BaseModel):
    title: str
    content: str
    tags: List[str]