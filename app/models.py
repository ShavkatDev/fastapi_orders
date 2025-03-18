from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # Базовый класс для моделей

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный идентификатор
    customer_name = Column(String, nullable=False)  # Имя клиента
    amount = Column(Float, nullable=False)  # Сумма заказа
    status = Column(String, default="pending")  # Статус заказа
    created_at = Column(DateTime, server_default=func.now())  # Дата создания
