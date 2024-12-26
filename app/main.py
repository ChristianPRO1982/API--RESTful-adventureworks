from fastapi import FastAPI, HTTPException, Depends
# from sqlmodel import Session
# from app.models import Product
# from app.database import get_session
from app.crud import get_products#, get_product_by_id, create_product, update_product, delete_product



app = FastAPI()


####################################################################################################
####################################################################################################
####################################################################################################

###########
### API ###
###########

@app.get("/products")
def list_products():
    products = get_products()
    return products


# @app.get("/products/{product_id}")
# def get_product(product_id: int, ):
#     product = get_product_by_id(session, product_id)
#     if product:
#         return product
#     raise HTTPException(status_code=404, detail="Product not found")


# @app.post("/products", response_model=Product)
# def create_new_product(product: Product, ):
#     created_product = create_product(session, product)
#     return created_product


# @app.put("/products/{product_id}")
# def update_product_info(product_id: int, product: Product, ):
#     updated_product = update_product(session, product_id, product)
#     if updated_product:
#         return updated_product
#     raise HTTPException(status_code=404, detail="Product not found")


# @app.delete("/products/{product_id}")
# def delete_product_info(product_id: int, ):
#     deleted_product = delete_product(session, product_id)
#     if deleted_product:
#         return {"message": "Product deleted"}
#     raise HTTPException(status_code=404, detail="Product not found")


####################################################################################################
####################################################################################################
####################################################################################################

############
### ROOT ###
############

@app.get("/")
def read_root():
    return {"message": "API AdventureWorks is running!"}
