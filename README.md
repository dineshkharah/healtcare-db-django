# 🏥 Healthcare Backend API (Django + DRF + PostgreSQL)

## 📌 Overview

This project is a backend system for a healthcare application built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.

It provides secure APIs for:

- User authentication (JWT-based)
- Managing patients and doctors
- Assigning doctors to patients

---

## 🚀 Features

- JWT Authentication (Register & Login)
- User-specific patient management
- Doctor management (CRUD)
- Patient-Doctor mapping system
- Protected APIs with authentication
- PostgreSQL database integration
- Environment variable configuration

---

## 🧱 Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Environment Management:** python-dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd healthcare
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env file

Create a .env file in the root directory:

```bash
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run server

```bash
python manage.py runserver
```

---

## 🔐 Authentication APIs

### Register

```bash
POST /api/auth/register/
```

### Request Body:

```bash
{
  "name": "test",
  "email": "test@example.com",
  "password": "123456"
}
```

##

### Login

```bash
POST /api/auth/login/
```

### Response:

```bash
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN",
  "user": {
    "id": 1,
    "name": "test",
    "email": "test@example.com"
  }
}
```

---

### Patient APIs (Authenticated)

| Method | Endpoint            | Description             |
| ------ | ------------------- | ----------------------- |
| POST   | /api/patients/      | Create patient          |
| GET    | /api/patients/      | Get all user’s patients |
| GET    | /api/patients/{id}/ | Get patient details     |
| PUT    | /api/patients/{id}/ | Update patient          |
| DELETE | /api/patients/{id}/ | Delete patient          |

---

### Doctor APIs (Authenticated)

| Method | Endpoint           | Description        |
| ------ | ------------------ | ------------------ |
| POST   | /api/doctors/      | Create doctor      |
| GET    | /api/doctors/      | Get all doctors    |
| GET    | /api/doctors/{id}/ | Get doctor details |
| PUT    | /api/doctors/{id}/ | Update doctor      |
| DELETE | /api/doctors/{id}/ | Delete doctor      |

---

### Patient-Doctor Mapping APIs (Authenticated)

| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| POST   | /api/mappings/              | Assign doctor to patient  |
| GET    | /api/mappings/              | Get all mappings          |
| GET    | /api/mappings/patient/{id}/ | Get doctors for a patient |
| DELETE | /api/mappings/{id}/         | Remove mapping            |

---

## 🔑 Authorization

All protected routes require:

```bash
Authorization: Bearer <access_token>
```

---

## Testing

All APIs were tested using Postman.

### Verified Features:

- Authentication flow
- User-specific data access
- Mapping constraints
- Error handling

---

## Author

Dinesh Kharah
