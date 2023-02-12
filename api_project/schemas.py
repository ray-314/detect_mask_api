"""Schema with type hints
"""

from pydantic import BaseModel
from typing import List

class Data(BaseModel):
    image: List

class Credentials(BaseModel):
    key: str

class Rectangles(BaseModel):
    top: int
    bottom: int
    left: int
    right: int

class WithMask(BaseModel):
    without_mask: float
    with_mask: float

class Pred(BaseModel):
    rectangles: List[Rectangles]
    tags: List[str]
    confidence: List[WithMask]