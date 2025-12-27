from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import secrets
import httpx

app = FastAPI()

AUTH_SERVICE_URL = "http://127.0.0.1:8000"
PRODUCT_SERVICE_URL = "http://127.0.0.1:8001"

class Order(BaseModel):
    token: str
    product_id: int

@app.post("/orders")
async def create_order(order: Order):

    async with httpx.AsyncClient() as client:
        # Validate token with Auth service
        auth_response = await client.get(f"{AUTH_SERVICE_URL}/validate", params={"token": order.token})

        if auth_response.status_code != 200:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Fetch product details from Product service
        product_response = await client.get(f"{PRODUCT_SERVICE_URL}/products/{order.product_id}")
        if product_response.status_code != 200:
            raise HTTPException(status_code=404, detail="Product not found")
        
        product_data = product_response.json()
        

    order_id = secrets.token_hex(8)

    return {
        "order_id": order_id,
        "message": "Order created successfully",
        "product": product_data
    }