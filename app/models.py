from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

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
