# Django Login DevOps Project

This is a simple **Django Login Application** created for practicing **DevOps tools and workflows**.

The project contains a basic login page with a Django backend and MySQL database.

---

## 🚀 Tech Stack

* Python
* Django
* MySQL
* Docker
* Git & GitHub
* Ubuntu Linux

---

## 📂 Project Structure

```
django-login-devops
│
├── project
│   ├── project
│   │   ├── settings.py
│   │   ├── urls.py
│   │
│   ├── users
│   │   ├── views.py
│   │   ├── urls.py
│   │
│   ├── templates
│   │   └── login.html
│   │
│   └── manage.py
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/django-login-devops.git
cd django-login-devops
```

---

### 2️⃣ Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```
python manage.py migrate
```

---

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/login
```

---

## 🐳 Docker (Next Step)

The project will also include:

* Dockerfile
* Docker Compose
* CI/CD pipeline

---

## 🎯 Goal

This project is created to practice **DevOps tools with a small Django application**.
