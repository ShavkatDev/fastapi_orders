# FastAPI Orders API 🚀

This is a FastAPI-based RESTful API for managing orders. It provides CRUD operations (Create, Read, Update, Delete) and uses PostgreSQL as the database with SQLAlchemy ORM. The database migrations are managed with Alembic.

## 🛠️ Features
- ✅ **CRUD operations** for orders (Create, Read, Update, Delete)
- ✅ **Asynchronous PostgreSQL database** using `asyncpg`
- ✅ **Pydantic models** for data validation
- ✅ **Alembic migrations** for database version control
- ✅ **Swagger UI (`/docs`) and ReDoc (`/redoc`)**
- ✅ **Dependency injection with `Depends()`**

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/ShavkatDev/fastapi_orders.git
cd fastapi_orders
```

### 2️⃣ Create and activate a virtual environment
```sh
# Windows
python -m venv venv
venv\Scripts\activate
# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables (`.env` file)
Create a `.env` file in the root directory and add:
```
DATABASE_URL=postgresql+asyncpg://postgres:yourpassword@localhost:5432/fastapi_orders
```
Replace `yourpassword` with your actual PostgreSQL password.

### 5️⃣ Run Alembic migrations
```sh
alembic upgrade head
```

### 6️⃣ Start the FastAPI server
```sh
uvicorn app.main:app --reload
```

---

## 📌 API Endpoints

| Method | Endpoint       | Description            |
|--------|--------------|------------------------|
| `POST` | `/orders/` | Create a new order |
| `GET`  | `/orders/` | Get all orders |
| `GET`  | `/orders/{id}` | Get a specific order by ID |
| `PUT`  | `/orders/{id}` | Update an existing order |
| `DELETE` | `/orders/{id}` | Delete an order |

---

## 📖 Documentation
- **Swagger UI**: [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)  
- **ReDoc**: [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)  

---

## 🎯 Author
**Shavkat**  
- GitHub: [ShavkatDev](https://github.com/ShavkatDev)  