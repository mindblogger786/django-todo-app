# ToDo Listing App

A simple To-Do listing application built with Django.

---

## 🎓 Key Features

### Server-Side (Django Backend)

* Add tasks with titles
* Mark tasks as completed
* Delete tasks
* Store tasks in a persistent database (SQLite by default)

---

## ⚙️ Technologies Used

* Python 3.13.4
* Django 5.1.11
* HTML5 / Bootstrap / CSS

---

## 📅 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo-django-app.git
cd todo-django-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔍 Project Structure

```
todo-django-app/
├── templates/
│   └── todos/
│       └── index.html
├── todos/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

---

## 🔧 Core Files Explained

### `models.py`

Defines the `ToDo` model with fields:

* `title`: task description
* `completed`: task status
* `created_at`: timestamp

### `views.py`

Contains logic to:

* Display tasks
* Add a new task
* Mark a task as completed
* Delete a single task
* Delete all tasks

---

## 📖 Learning Objectives

* Understand Django MVT architecture
* Practice CRUD operations

---

## 🚀 Next Steps (Ideas for Enhancement)

* Add user login & registration (authentication)
* Make it a Progressive Web App (PWA)
* Use AJAX for asynchronous operations
* Add task categories or deadlines

---

## 🌟 Author

```
**Piyush**
Web Developer | Tech Enthusiast
```

---

## ✉️ License

This project is made for academic and learning purposes. Feel free to use.
