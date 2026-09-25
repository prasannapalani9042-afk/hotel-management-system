# 🏨 Hotel Management System

A full-stack **Hotel Management System** built with Flask, SQLite, SQLAlchemy, Flask-Login, HTML, CSS and JavaScript.

## ✨ Modules

- 🛏️ Hotel room browsing and booking
- 🍽️ Food menu, room service and order tracking
- ⭐ Reviews, ratings and complaints
- 🎮 Quiz game with levels, timer, coins and leaderboard
- 📋 Attendance management for teachers and students
- 👥 Role-based access for Admin, Teacher, Student and Guest

## 🛠️ Tech Stack

- **Backend:** Python + Flask
- **Database:** SQLite + Flask-SQLAlchemy
- **Authentication:** Flask-Login
- **Frontend:** HTML5 + CSS3 + JavaScript + Jinja2

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/hotel-management-system.git
cd hotel-management-system
```

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the secret key

Copy `.env.example` to `.env` and set a secure `SECRET_KEY`.

For a quick local demo, the application also has a development fallback secret.

### 5. Seed sample data

```bash
python seed.py
```

### 6. Start the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 🔐 Demo Accounts

These accounts are created by `seed.py` for local/demo use:

| Role | Email | Password |
|---|---|---|
| Admin | admin@hotel.com | admin123 |
| Teacher | teacher@hotel.com | teacher123 |
| Student | student1@hotel.com | student123 |
| Guest | guest@hotel.com | guest123 |

> Change or remove demo credentials before using the application in production.

## 📁 Project Structure

```text
hotel-management-system/
├── app.py
├── config.py
├── models.py
├── seed.py
├── requirements.txt
├── .env.example
├── .gitignore
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py
│   ├── booking_routes.py
│   ├── service_routes.py
│   ├── review_routes.py
│   ├── quiz_routes.py
│   └── attendance_routes.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── booking/
│   ├── services/
│   ├── reviews/
│   ├── quiz/
│   └── attendance/
└── static/
    └── css/
        └── style.css
```

## 🗃️ Database

The default database is SQLite and is created under `instance/hotel.db` after setup. The `instance/` folder is intentionally ignored by Git so local database files are not committed.

## 🌐 GitHub Upload

```bash
git init
git add .
git commit -m "Initial Hotel Management System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hotel-management-system.git
git push -u origin main
```

## 📌 Future Improvements

- Email notifications
- Room and food image uploads
- Payment gateway integration
- PDF reports
- Production deployment
