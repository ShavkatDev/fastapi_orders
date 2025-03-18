from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db
from app.schemas import OrderCreate, OrderUpdate, OrderResponse
from app.crud import create_order, get_order, get_orders, update_order, delete_order

router = APIRouter(prefix="/orders", tags=["orders"])


# Создать заказ
@router.post("/", response_model=OrderResponse)
async def create_order_api(order_data: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await create_order(db, order_data)


# Получить все заказы
@router.get("/", response_model=List[OrderResponse])
async def get_orders_api(db: AsyncSession = Depends(get_db)):
    return await get_orders(db)


# Получить заказ по ID
@router.get("/{order_id}", response_model=OrderResponse)
async def get_order_api(order_id: int, db: AsyncSession = Depends(get_db)):
    order = await get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


# Обновить заказ
@router.put("/{order_id}", response_model=OrderResponse)
async def update_order_api(order_id: int, order_data: OrderUpdate, db: AsyncSession = Depends(get_db)):
    order = await update_order(db, order_id, order_data)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


# Удалить заказ
@router.delete("/{order_id}", response_model=dict)
async def delete_order_api(order_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return {"message": "Заказ удалён"}
