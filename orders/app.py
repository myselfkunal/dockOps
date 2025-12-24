from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import secrets
import httpx

app = FastAPI()

PRODUCT_SERVICE_URL = "http://127.0.0.1:8001"

class Order(BaseModel):
    token: str
    product_id: int

@app.post("/orders")
async def create_order(order: Order):
    
    if "-" not in order.token:
        raise HTTPException(status_code=400, detail="Invalid token ")
 
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{order.product_id}")

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Product not found")

    product = response.json()
    order_id=secrets.token_hex(8)

    return {
        "order_id": order_id,
        "product": product,
        "status": "Order placed successfully"
    }