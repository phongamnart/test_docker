from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    barcode: str
    name_product: str
    price: float

products = []

@app.get("/")
def index():
    return products

# Add product POST
@app.post("/add-product/")
def add_product(product: Product):
    products.append(product)
    return {"message": f"Product {product.name_product} has been added."}

# Edit product PUT
@app.put("/update-product/{product_name}")
def update_product(product_name: str, updated_product: Product):
    for i, product in enumerate(products):
        if product.name_product == product_name:
            products[i] = updated_product
            return {"message": f"Product {product_name} has been updated."}
    return {"error": f"Product {product_name} not found."}

# Delete product DELETE
@app.delete("/delete-product/{product_name}")
def delete_product(product_name: str):
    for product in products:
        if product.name_product == product_name:
            products.remove(product)
            return {"message": f"Product {product_name} has been deleted."}
    return {"error": f"Product {product_name} not found."}

# All product GET
@app.get("/products/")
def get_products():
    return {"products": [product.dict() for product in products]}
