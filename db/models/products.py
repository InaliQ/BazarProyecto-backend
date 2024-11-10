from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    _id:Optional[str]
    id: Optional[str]
    title: str
    description: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    brand: str
    category: str
    thumbnail: str
    images: List[str] = []