from fastapi import APIRouter, HTTPException, status
from typing import List
from db.models.products import ProductModel
from db.schemas.products import product_schema, products_schema
from db.client import bazar_collection  # Este sigue siendo necesario
from bson import ObjectId

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
)

# Ruta para obtener todos los productos
@router.get("/", response_model=List[ProductModel])
async def get_all_products():
    try:
        # Accede a los documentos en la colección 'bazar'
        documents = list(bazar_collection.find())
        
        # Extrae los productos de cada documento
        all_products = []
        for doc in documents:
            # Asegúrate de que el campo 'products' exista y agregarlo a la lista
            products = doc.get("products", [])
            all_products.extend(products)  # Añadir todos los productos en la lista final
        
        print(f"Productos encontrados: {all_products}")  # Verifica los productos
        
        # Ahora devuelve los productos usando el esquema
        return products_schema(all_products)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ruta para obtener un producto por su ID
@router.get("/{product_id}", response_model=ProductModel)
async def get_product(product_id: str):
    try:
        # Buscar en los productos dentro de la colección 'bazar'
        documents = list(bazar_collection.find())
        for doc in documents:
            # Accede al campo 'products'
            products = doc.get("products", [])
            # Busca el producto por su _id dentro del campo 'products'
            product = next((prod for prod in products if str(prod["id"]) == product_id), None)
            if product:
                return product_schema(product)
        
        # Si no se encuentra el producto, lanza error 404
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
