from sqlmodel import SQLModel, Field
from typing import Optional



class Product(SQLModel, table=True):
    productid: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(sa_column_kwargs={"unique": True})
    productnumber: str = Field(sa_column_kwargs={"unique": True})
    color: str
    standardcost: float
    listprice: float
    size: float
    weight: float
    productmodelid: Optional[int] = Field(default=None, foreign_key="productmodel.productmodelid")
    productcategoryid: Optional[int] = Field(default=None, foreign_key="productcategory.productcategoryid")
    sellstartdate: Optional[str] = Field(default=None)
    sellenddate: Optional[str] = Field(default=None)
    discontinueddate: Optional[str] = Field(default=None)
    thumbnailphoto: Optional[bytes] = Field(default=None)
    thumbnailphotofilename: Optional[str] = Field(default=None)
    rowguid: Optional[str] = Field(default=None)
    modifieddate: Optional[str] = Field(default=None)
