from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    id: str
    productId: str
    title: str
    price: float
    image: str
    description: str
    quantity: int

class SaleModel(BaseModel):
    id: str
    fecha: str  # o `datetime` si prefieres objetos de fecha
    total: float
    productos: List[ProductModel] = []
