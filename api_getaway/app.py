from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

PRODUCTS_SERVICE_URL = "http://products_service:8000"
ORDERS_SERVICE_URL = "http://orders_service:8000"

@app.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCTS_SERVICE_URL}/products")
    return response.json()

@app.post("/orders")
async def create_order(product_id: int, quantity: int):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{ORDERS_SERVICE_URL}/orders",
            json={"product_id": product_id, "quantity": quantity}
        )
    return response.json()