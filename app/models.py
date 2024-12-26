from sqlmodel import SQLModel, Field
from typing import Optional



class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    product_number: str
    make_flag: bool
    finished_goods_flag: bool
    color: Optional[str] = None
    safety_stock_level: int
    reorder_point: int
    standard_cost: float
    list_price: float
    days_to_manufacture: int
    sell_start_date: str
    sell_end_date: Optional[str] = None
