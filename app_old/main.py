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

@app.get(
    "/products",
    summary="List of products",
    description=(
        "List all products with their details."
    ),
    tags=["Produits"],  # Permet d'organiser par catégories dans la doc Swagger
    responses={
        200: {
            "description": "Liste de tous les produits.",
            "content": {
                "application/json": {
                    "example": [
                                {
                                    "ProductID": 748,
                                    "Name": "HL Mountain Frame - Silver, 38",
                                    "ProductNumber": "FR-M94S-38",
                                    "MakeFlag": True,
                                    "FinishedGoodsFlag": True,
                                    "Color": "Silver",
                                    "SafetyStockLevel": 500,
                                    "ReorderPoint": 375,
                                    "StandardCost": 747.2002,
                                    "ListPrice": 1364.5,
                                    "Size": "38",
                                    "SizeUnitMeasureCode": "CM ",
                                    "WeightUnitMeasureCode": "LB ",
                                    "Weight": 2.68,
                                    "DaysToManufacture": 2,
                                    "ProductLine": "M ",
                                    "Class": "H ",
                                    "Style": "U ",
                                    "ProductSubcategoryID": 12,
                                    "ProductModelID": 5,
                                    "SellStartDate": "2011-05-31T00:00:00",
                                    "SellEndDate": "NaT",
                                    "DiscontinuedDate": None,
                                    "rowguid": "F246ACAA-A80B-40EC-9208-02EDEF885129",
                                    "ModifiedDate": "2014-02-08T10:01:36.827000",
                                    "ProductCategoryName": None,
                                    "ProductCategoryrowguid": None,
                                    "ProductCategoryModifiedDate": "NaT",
                                    "ProductModel": [
                                    {
                                        "Name": "HL Mountain Frame",
                                        "CatalogDescription": None,
                                        "Instructions": None,
                                        "rowguid": "FDD5407B-C2DB-49D1-A86B-C13A2E3582A2",
                                        "ModifiedDate": "2011-05-01T00:00:00",
                                        "pmpdc_productdescriptionid": 647,
                                        "pmpdc_cultureid": "en    ",
                                        "pmpdc_modifieddate": "2013-04-30T00:00:00",
                                        "pd_description": "Each frame is hand-crafted in our Bothell facility to the optimum diameter and wall-thickness required of a premium mountain frame. The heat-treated welded aluminum frame has a larger diameter tube that absorbs the bumps.",
                                        "pd_rowguid": "7AD9E29F-16CF-4DB0-B073-CC62D501B61A",
                                        "pd_modifieddate": "2013-04-30T00:00:00"
                                    }
                                    ]
                                },
                    ]
                }
            },
        },
        500: {"description": "Erreur serveur si la connexion échoue"},
    },
)
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
