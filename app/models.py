from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid



####################################################################################################
####################################################################################################
####################################################################################################

###############
### PRODUCT ###
###############

class Product(SQLModel, table=True):
    ProductID: int = Field(default=None, primary_key=True)  # Clé primaire
    Name: str = Field(max_length=100)
    ProductNumber: str = Field(max_length=50)
    MakeFlag: bool
    FinishedGoodsFlag: bool
    Color: Optional[str] = Field(default=None, max_length=30)
    SafetyStockLevel: int
    ReorderPoint: int
    StandardCost: float
    ListPrice: float
    Size: Optional[str] = Field(default=None, max_length=10)
    SizeUnitMeasureCode: Optional[str] = Field(default=None, max_length=6)
    WeightUnitMeasureCode: Optional[str] = Field(default=None, max_length=6)
    Weight: Optional[float] = None
    DaysToManufacture: int
    ProductLine: Optional[str] = Field(default=None, max_length=4)
    Class: Optional[str] = Field(default=None, max_length=4)
    Style: Optional[str] = Field(default=None, max_length=4)
    ProductSubcategoryID: Optional[int] = None
    ProductModelID: Optional[int] = None
    SellStartDate: datetime
    SellEndDate: Optional[datetime] = None
    DiscontinuedDate: Optional[datetime] = None
    rowguid: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False)
    ModifiedDate: datetime



#########################
### PRODUCT CATEGORY ###
########################

class ProductCategory(SQLModel, table=True):
    ProductCategoryID: int = Field(default=None, primary_key=True)
    Name: str = Field(max_length=100)
    rowguid: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False)
    ModifiedDate: datetime


#####################
### PRODUCT MODEL ###
#####################

class ProductModel(SQLModel, table=True):
    ProductModelID: int = Field(default=None, primary_key=True)
    Name: str = Field(max_length=100)
    CatalogDescription: Optional[str] = None  # Utilisation de str pour stocker l'XML
    Instructions: Optional[str] = None  # Stockage de l'XML en tant que texte
    rowguid: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False)
    ModifiedDate: datetime


#################################
### PRODUCT MODEL DESCRIPTION ###
#################################

class ProductModelProductDescriptionCulture(SQLModel, table=True):
    ProductModelID: int = Field(default=None, primary_key=True)
    ProductDescriptionID: int = Field(default=None, primary_key=True)
    CultureID: str = Field(max_length=12)
    ModifiedDate: datetime


###########################
### PRODUCT DESCRIPTION ###
###########################

class ProductDescription(SQLModel, table=True):
    ProductDescriptionID: int = Field(default=None, primary_key=True)
    Description: str = Field(max_length=800)
    rowguid: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=False)
    ModifiedDate: datetime