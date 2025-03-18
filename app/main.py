from fastapi import FastAPI
from app.routes import orders

app = FastAPI(title="Orders API")

# Подключаем маршруты
app.include_router(orders.router)
