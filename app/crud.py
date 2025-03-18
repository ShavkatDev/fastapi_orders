from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Order
from app.schemas import OrderCreate, OrderUpdate
from typing import List, Optional



# Функция для создания заказа
async def create_order(db: AsyncSession, order_data: OrderCreate) -> Order:
    new_order = Order(**order_data.model_dump())
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order


# Функция для получения заказа по ID
async def get_order(db: AsyncSession, order_id: int) -> Optional[Order]:
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalars().first()


# Функция для получения всех заказов
async def get_orders(db: AsyncSession) -> List[Order]:
    result = await db.execute(select(Order))
    return result.scalars().all()


# Функция для обновления заказа
async def update_order(db: AsyncSession, order_id: int, order_data: OrderUpdate) -> Optional[Order]:
    order = await get_order(db, order_id)
    if not order:
        return None

    for key, value in order_data.model_dump(exclude_unset=True).items():
        setattr(order, key, value)

    await db.commit()
    await db.refresh(order)
    return order


# Функция для удаления заказа
async def delete_order(db: AsyncSession, order_id: int) -> bool:
    order = await get_order(db, order_id)
    if not order:
        return False

    await db.delete(order)
    await db.commit()
    return True