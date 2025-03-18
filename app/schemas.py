from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class OrderBase(BaseModel):
    customer_name: str
    amount: float
    status: Optional[str] = "pending"
    phone_number: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[str] = None


class OrderResponse(OrderBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True