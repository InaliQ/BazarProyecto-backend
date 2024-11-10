from pymongo.mongo_client import MongoClient

# Conectar al cliente MongoDB con URI
#uri = "mongodb+srv://inali:inali@bazar.guoid.mongodb.net/?retryWrites=true&w=majority&appName=bazar"
uri = "mongodb+srv://inali:inali@bazar.guoid.mongodb.net/?retryWrites=true&w=majority&appName=bazar"
client = MongoClient(uri)

db = client["bazar-universal"]  # Asegúrate de que esta es la base de datos correcta
bazar_collection = db["bazar"]
productos_collection = db["products"]

# Verificar los documentos en la colección
documents = list(bazar_collection.find())


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error al conectar con MongoDB:", e)
