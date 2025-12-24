from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Phone", "price": 35000},
    {"id": 3, "name": "Headphones", "price": 3000},
    {"id": 4, "name": "Keyboard", "price": 2500},
]

@app.get("/products")
async def list_products():
    return products

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}
    
