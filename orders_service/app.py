from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# DB falsa (en memoria)
orders_db = []

class Order(BaseModel):
    product_id: int
    quantity: int

@app.post("/orders")
def create_order(order: Order):
    new_order = {"id": len(orders_db) + 1, **order.dict()}
    orders_db.append(new_order)
    return new_order

@app.get("/orders")
def get_orders():
    return orders_db