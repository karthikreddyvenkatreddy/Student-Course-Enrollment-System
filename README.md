# 🎓 Student Course Enrollment System

A RESTful Student Course Enrollment System built using **FastAPI**, **SQLAlchemy**, and **MySQL** with **JWT Authentication**. The application allows users to securely register, log in, and manage student course enrollments through CRUD operations.

---

## 🚀 Features

- User Registration
- Secure User Login with JWT Authentication
- Create Student Enrollments
- View All Enrollments
- Search and Filter Enrollments
- Pagination Support
- Update Enrollment Details
- Delete Enrollments
- MySQL Database Integration
- Interactive API Documentation (Swagger UI)

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- SQLAlchemy ORM
- MySQL
- JWT Authentication
- Passlib (Password Hashing)
- Pydantic

### Tools
- Uvicorn
- Swagger UI
- Git & GitHub
- VS Code

---

## 📂 Project Structure

```
backend/
│
├── auth.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/karthikreddyvenkatreddy/Student-Course-Enrollment-System.git
```

### 2. Navigate to the project

```bash
cd Student-Course-Enrollment-System/backend
```

### 3. Create Virtual Environment

```bash
python -m venv myvenv
```

### 4. Activate Virtual Environment

Windows

```bash
myvenv\Scripts\activate
```

Linux / macOS

```bash
source myvenv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

Create a `.env` file inside the backend folder.

Example:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/studentdb

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Update the database credentials according to your local MySQL server.

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Server starts at

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Login and receive JWT Token |

### Enrollment

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /enrollments | Create Enrollment |
| GET | /enrollments | Get All Enrollments |
| GET | /enrollments/{id} | Get Enrollment by ID |
| PUT | /enrollments/{id} | Update Enrollment |
| DELETE | /enrollments/{id} | Delete Enrollment |

---

## 🔍 Filtering

The API supports filtering using query parameters.

Example:

```
GET /enrollments?course_name=Python
```

```
GET /enrollments?payment_status=Paid
```

```
GET /enrollments?enrollment_status=Active
```

---

## 📄 Pagination

```
GET /enrollments?skip=0&limit=10
```

---

## 🔐 Authentication

Protected endpoints require a JWT Bearer Token.

1. Register a user.
2. Login using the registered credentials.
3. Copy the generated access token.
4. Click **Authorize** in Swagger UI.
5. Enter:

```
Bearer <your_access_token>
```

---

## 📦 Dependencies

- FastAPI
- SQLAlchemy
- Uvicorn
- PyMySQL
- Python-Jose
- Passlib
- Bcrypt
- Python-Multipart
- Pydantic
- python-dotenv

---

## 🎯 Learning Outcomes

- FastAPI REST API Development
- JWT Authentication
- SQLAlchemy ORM
- MySQL Database Integration
- CRUD Operations
- Password Hashing
- API Testing using Swagger UI
- Dependency Injection
- Pagination and Filtering
- Secure Backend Development

---

## 👨‍💻 Author

**Karthik Reddy Venkat Reddy**

GitHub:
https://github.com/karthikreddyvenkatreddy

---

## 📜 License

This project is developed for educational and learning purposes.
