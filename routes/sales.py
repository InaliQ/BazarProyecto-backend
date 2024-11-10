from fastapi import APIRouter, HTTPException, status
from db.client import bazar_collection  # Asegúrate de que esto se conecta a tu base de datos
from db.models.sales import SaleModel
from db.schemas.sales import sale_schema
from typing import List
import logging

router = APIRouter(
    prefix="/sales",
    tags=["sales"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
)

# POST: Guardar la venta
@router.post("/", response_model=SaleModel)
async def registrar_venta(venta: SaleModel):
    try:
        existing_sale = bazar_collection.find_one({"ventas": {"$exists": True}})
        
        if existing_sale:
            bazar_collection.update_one(
                {},  # Actualizamos el primer documento encontrado (ventas)
                {"$push": {"sales": venta.dict()}}  # Usamos "$push" para agregar la venta
            )
            
            bazar_collection.update_one(
            {},  # Se actualiza el primer documento encontrado (el carrito)
            {"$set": {"shopCar": []}}  # Usamos "$set" para vaciar el carrito
        )
        else:
            bazar_collection.insert_one({
                "ventas": [venta.dict()]  # Insertamos la venta como un nuevo documento
            })
        
        return venta
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")



# GET: Obtener todas las ventas
@router.get("/", response_model=List[SaleModel])
async def obtener_ventas():
    try:
        ventas = list(bazar_collection.find())
        
        ventas_list = []
        for venta in ventas:
            ventas = venta.get("sales", [])
            for v in ventas:
                # Si "productos" son objetos completos, no cadenas
                productos = [
                    {
                        "id": p.get("id"),
                        "productId": p.get("productId"),
                        "title": p.get("title"),
                        "price": p.get("price"),
                        "image": p.get("image"),
                        "description": p.get("description"),
                        "quantity": p.get("quantity")
                    }
                    for p in v.get("productos", [])
                ]
                v["productos"] = productos
                ventas_list.append(v)
        return ventas_list

    except Exception as e:
        logging.error(f"Error al obtener ventas: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))





