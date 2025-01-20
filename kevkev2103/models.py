from sqlmodel import SQLModel, Field
from typing import Optional


# Table Product
class Product(SQLModel, table=True):
    __tablename__= "Product"
    __table_args__ = {"schema": "Production"}
    ProductID: int = Field(default=None, primary_key=True)
    Name: str
    ProductNumber: str
    ListPrice: float
    StandardCost: float
    SellStartDate: Optional[str] = None  # Exemple d'attribut de type date

# Table SalesOrderHeader (En-tête de commande)
class SalesOrderHeader(SQLModel, table=True):
    SalesOrderID: int = Field(default=None, primary_key=True)
    CustomerID: int = Field(foreign_key="customer.CustomerID")
    OrderDate: Optional[str] = None
    TotalDue: float

# Table SalesOrderDetail (Détail de commande)
class SalesOrderDetail(SQLModel, table=True):
    SalesOrderID: int = Field(foreign_key="salesorderheader.SalesOrderID", primary_key=True)
    SalesOrderDetailID: int = Field(default=None, primary_key=True)
    ProductID: int = Field(foreign_key="product.ProductID")
    OrderQty: int
    UnitPrice: float
    LineTotal: float

# Table ProductCategory
class ProductCategory(SQLModel, table=True):
    ProductCategoryID: int = Field(default=None, primary_key=True)
    Name: str
    ParentProductCategoryID: Optional[int] = Field(default=None, foreign_key="productcategory.ProductCategoryID")