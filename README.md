# 🎉 Event Management Web App

![Django](https://img.shields.io/badge/Django-6.0-green)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📌 Description

A web application built with Django to manage events, participants, and registrations.

---

## 🚀 Features

### 👤 Authentication

* Register
* Login / Logout

### 📅 Events

* Create / Update / Delete events
* View event list
* View event details

### 🙋 Participation

* Join event
* Cancel participation
* View participants

### 📍 Locations

* Assign location to events

---

## 🖼️ Screenshots

### Login
![Login](screenshots/login.png)

### Event List
![Event List](screenshots/event_list.png)

### Event Detail
![Event Detail](screenshots/event_detail.png)

### Add Event
![Add Event](screenshots/add_event.png)

### Stats
![Stats](screenshots/stats.png)

## 🛠️ Tech Stack

* Python
* Django
* HTML / CSS
* SQLite

---

## ⚙️ Installation

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🌐 Usage

Open your browser:

```
http://127.0.0.1:8000
```

---

## 🔑 Admin Panel

```
http://127.0.0.1:8000/admin
```

---

## ⚠️ Notes

* Do NOT include `env/`
* Run `migrate` before starting
* Create a user to access the app

---

## 👨‍💻 Author

**Mahrouk Walid Ibrahim** 🚀

---

## ⭐ Future Improvements

* Better UI (Bootstrap)
* Role management
* Notifications
* Statistics dashboard
