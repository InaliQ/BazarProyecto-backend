from pydantic import BaseModel
from typing import Optional

class ShopCarModel(BaseModel):
    productId: str
    title: str
    price: float
    image: str
    description: str
    quantity: int

