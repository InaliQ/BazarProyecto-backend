def sale_schema(sale) -> dict:
    return {
        "id": str(sale["_id"]) if "_id" in sale else None,
        "fecha": sale.get("fecha", ""),
        "total": sale.get("total", 0.0),
        "productos": [
            {
                "id": product.get("id"),
                "productId": product.get("productId"),
                "title": product.get("title"),
                "price": product.get("price"),
                "image": product.get("image"),
                "description": product.get("description"),
                "quantity": product.get("quantity")
            }
            for product in sale.get("productos", [])
        ]
    }
