


def product_schema(product) -> dict:
    return {
        "_id": str(product["_id"]) if "_id" in product else None,
        "id": product.get("id"),
        "title": product.get("title", ""),
        "description": product.get("description", ""),
        "price": product.get("price", 0.0),
        "discountPercentage": product.get("discountPercentage", 0.0),
        "rating": product.get("rating", 0.0),
        "stock": product.get("stock", 0),
        "brand": product.get("brand", ""),
        "category": product.get("category", ""),
        "thumbnail": product.get("thumbnail", ""),
        "images": product.get("images", []),
    }

    
def products_schema(products) -> list:
    return [product_schema(product) for product in products]