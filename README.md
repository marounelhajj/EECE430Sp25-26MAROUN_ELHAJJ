# 🏐 VolleyPlayerList – Django CRUD Project

A full-stack Django application to manage a volleyball player roster with Add, Read, Update, and Delete (CRUD) operations.

---

## 📁 Project Structure

```
volleyball_project/
│
├── manage.py
├── requirements.txt
│
├── volleyball_project/          ← Django project config
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
│
└── volley_app/                  ← Main application
    ├── __init__.py
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── volley_app/
            ├── base.html
            ├── player_list.html
            ├── player_detail.html
            ├── player_form.html
            └── player_confirm_delete.html
```

---

## 🚀 Setup Steps (Run in Terminal)

### Step 1 – Install Django
```bash
pip install django
```

### Step 2 – Navigate into the project folder
```bash
cd volleyball_project
```

### Step 3 – Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4 – (Optional) Create admin superuser
```bash
python manage.py createsuperuser
```

### Step 5 – Start the development server
```bash
python manage.py runserver
```

### Step 6 – Open in browser
```
http://127.0.0.1:8000/
```

Admin panel (if you created a superuser):
```
http://127.0.0.1:8000/admin/
```

---

## 🌐 URL Routes

| URL                        | View              | Description              |
|----------------------------|-------------------|--------------------------|
| `/`                        | player_list       | List all players         |
| `/player/<id>/`            | player_detail     | View one player          |
| `/player/add/`             | player_create     | Add a new player         |
| `/player/<id>/edit/`       | player_update     | Edit existing player     |
| `/player/<id>/delete/`     | player_delete     | Delete a player          |

---

## 🗄️ Player Model Fields

| Field           | Type          | Description                          |
|-----------------|---------------|--------------------------------------|
| id              | AutoField     | Auto-generated primary key           |
| name            | CharField     | Full name of the player              |
| date_joined     | DateField     | When the player joined               |
| position        | CharField     | Playing position (choice field)      |
| salary          | DecimalField  | Monthly/annual salary payment        |
| contact_person  | CharField     | Emergency/agent contact name         |
| contact_phone   | CharField     | Contact phone number (optional)      |
| contact_email   | EmailField    | Contact email address (optional)     |

### Position Choices:
- Setter
- Outside Hitter
- Opposite Hitter
- Middle Blocker
- Libero
- Defensive Specialist
