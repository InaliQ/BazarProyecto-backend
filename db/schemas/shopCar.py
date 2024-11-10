def shop_car_schema(shop_car) -> dict:
    return {
        "productId": shop_car.get("productId"),
        "title": shop_car.get("title", ""),
        "price": shop_car.get("price", 0.0),
        "image": shop_car.get("image", ""),
        "description": shop_car.get("description", ""),
        "quantity": shop_car.get("quantity", 1),
    }

def shop_cars_schema(shop_cars) -> list:
    return [shop_car_schema(shop_car) for shop_car in shop_cars]
