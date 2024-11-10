from typing import List
from pydantic import BaseModel
from db.models.shopCar import ShopCarModel 
from fastapi import APIRouter, HTTPException, status
from db.schemas.shopCar import shop_car_schema, shop_cars_schema

from typing import List
from db.client import bazar_collection  # Este sigue siendo necesario



router = APIRouter(
    prefix="/shopCar",
    tags=["shopCar"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
    
)


@router.post("/", response_model=ShopCarModel)
async def add_to_cart(item: ShopCarModel):
    try:
        existing_cart = bazar_collection.find_one({"shopCar": {"$exists": True}})
        
        if existing_cart:
            bazar_collection.update_one(
                {},  # Actualizamos el primer documento encontrado (el carrito)
                {"$push": {"shopCar": item.dict()}}  # Usamos "$push" para agregar el producto
            )
        else:
            # Si no existe, creamos un nuevo carrito con el primer producto
            bazar_collection.insert_one({
                "shopCar": [item.dict()]  # Insertamos el carrito con el primer producto
            })

        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


        
    
    
#get Todo
@router.get("/", response_model=List[ShopCarModel])
async def get_cart():
    try: 
        documents = list(bazar_collection.find())
        
        all_shopCar = []
        for doc in documents:
            shopCar  = doc.get("shopCar", [])
            all_shopCar.extend(shopCar)
        print(f"Productos encontrados: {all_shopCar}")
        return shop_cars_schema(all_shopCar)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    #Eliminar del carrito 
@router.delete("/{product_id}")
async def delete_from_cart(product_id: str):
    result = bazar_collection.update_one(
        {},
        {"$pull": {"shopCar": {"productId": product_id}}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado en el carrito"
        )
    return {"message": "Producto eliminado del carrito"} 