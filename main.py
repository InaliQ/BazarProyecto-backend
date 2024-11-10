import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products, shopCar, sales
from fastapi.staticfiles import StaticFiles

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados HTTP
)

@app.get("/")
async def root():
    return {"message": "Hello World"} 

app.include_router(products.router)
app.include_router(shopCar.router)
app.include_router(sales.router)



if __name__ == "__main__":
    # Obtenemos el puerto desde la variable de entorno o usamos el 8000 por defecto
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
