# 💰 Expense Tracker

A simple and elegant web-based Expense Tracker built using **Flask**, **SQLite**, **SQLAlchemy**, and **HTML/CSS**, designed with a RESTful API structure.  
Track your daily expenses — add, view, and delete expenses easily through clean UI and modular endpoints.

---

## 🔧 Features

- 🔐 User Registration & Login (Session-based)
- 📝 Add Expense via Web Form or POST request
- 📋 View Expenses (Linked to Logged-in User)
- 🗑️ Delete Expense (via API POST endpoint)
- 🌐 RESTful API structure** for all internal operations
- 🎨 Emoji-enhanced UI with clean layout

---

## 📡 REST API Endpoints

| Method | Endpoint            | Description                      |
|--------|---------------------|----------------------------------|
| POST   | `/register`         | Register a new user              |
| POST   | `/login`            | Authenticate existing user       |
| GET    | `/`                 | View all user expenses (dashboard) |
| GET    | `/add`              | Show form to add expense         |
| POST   | `/add`              | Submit new expense               |
| POST   | `/delete/<id>`      | Delete a specific expense by ID  |
| GET    | `/logout`           | Logout current session           |

> 💡 Note: These endpoints are not public APIs — they power the internal routing of the app with REST principles.

---

## 🛠️ Tech Stack

| Frontend | Backend | Database | Architecture |
|----------|---------|----------|--------------|
| HTML + CSS | Flask (Python) | SQLite + SQLAlchemy | RESTful Routes |

---

## 📁 Project Structure

```
expense_tracker/
│
├── app.py               # Main app file and routes
├── api.py               # REST API routes (optional future use)
├── auth.py              # Blueprint for authentication (login/register)
├── models.py            # SQLAlchemy models (User, Expense)
│
├── templates/           # All HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── add_expense.html
│
├── static/              # Static files (CSS, images, etc.)
│   └── style.css
│
├── requirements.txt     # All required Python packages
└── README.md            # Project overview and instructions

---

## 🚀 Getting Started

1. **Clone the repo:**
```bash
git clone https://github.com/ForStudy7se/expense-tracker.git
cd expense_tracker
```

2. **Create and activate virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
```

3. **Install requirements:**
```bash
pip install -r requirements.txt
```

4. **Initialize database:**
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

5. **Run the server:**
```bash
python app.py
```

6. **Open browser:**
```
http://127.0.0.1:5000
```

---

## ✅ Future Plans

- 📊 Add filters and category-wise charts
- 📁 Export data to Excel/CSV
- 📱 Mobile-friendly responsive layout
- 🧪 Separate REST API version with token auth (optional)

---

## 🙋‍♀️ Made by

KIRTI VISPUTE — with ❤️ and Flask.  
[GitHub](https://github.com/ForStudy7se)
