from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# DB falsa (en memoria)
products_db = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 19.99},
]

@app.get("/products")
def get_products():
    return products_db

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return next((p for p in products_db if p["id"] == product_id), None)