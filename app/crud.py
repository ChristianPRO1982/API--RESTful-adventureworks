from sqlalchemy.sql import text
from sqlmodel import Session, select
from typing import List, Optional
import datetime
from app.models import Product, ProductCategory, ProductModel, ProductModelProductDescriptionCulture, ProductDescription



####################################################################################################
####################################################################################################
####################################################################################################

######################
### CREATE PRODUCT ###
######################

def create_product(db: Session, name: str, product_number: str, make_flag: bool, finished_goods_flag: bool, 
                   safety_stock_level: int, reorder_point: int, standard_cost: float, list_price: float, 
                   sell_start_date: str) -> Product:
    db_product = Product(
        Name=name,
        ProductNumber=product_number,
        MakeFlag=make_flag,
        FinishedGoodsFlag=finished_goods_flag,
        SafetyStockLevel=safety_stock_level,
        ReorderPoint=reorder_point,
        StandardCost=standard_cost,
        ListPrice=list_price,
        SellStartDate=sell_start_date,
        ModifiedDate=datetime.utcnow(),
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int) -> Optional[Product]:
    return db.query(Product).filter(Product.ProductID == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10) -> List[Product]:
    return (
        db.query(Product)
        .from_statement(text('SELECT * FROM production.product'))
        .all()
    )
    from sqlalchemy.sql import text

def update_product(db: Session, product_id: int, name: Optional[str], product_number: Optional[str]) -> Product:
    db_product = db.query(Product).filter(Product.ProductID == product_id).first()
    if name:
        db_product.Name = name
    if product_number:
        db_product.ProductNumber = product_number
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.ProductID == product_id).first()
    db.delete(db_product)
    db.commit()
