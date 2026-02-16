from pydantic import BaseModel
import uuid
from typing import List


class Article(BaseModel):
    id: int = uuid.uuid4()
    title: str
    content: str
    tags: List[str]