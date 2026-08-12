# SubWatch Backend

Django + Django REST Framework API backend for **SubWatch**, a subscription tracker app.

## Tech Stack

| Layer           | Technology                            |
| --------------- | ------------------------------------- |
| Framework       | Django 6.1                            |
| API             | Django REST Framework 3.18            |
| Auth            | djangorestframework-simplejwt (JWT)   |
| CORS            | django-cors-headers                   |
| Database        | PostgreSQL (SQLite fallback for dev)  |
| Config          | python-decouple (`.env` file)         |

## Quick Start

```bash
# 1. Clone the repo
git clone <repo-url> subwatch-backend
cd subwatch-backend

# 2. Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env (optional — SQLite works without any env vars)
cp .env.example .env
# Edit .env to taste; defaults are fine for local dev

# 5. Run database migrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver
# → http://localhost:8000/
```

## Environment Variables

See [`.env.example`](.env.example) for the full list. All variables have sensible defaults so you can boot the project with zero configuration.

| Variable               | Default                          | Description                     |
| ---------------------- | -------------------------------- | ------------------------------- |
| `SECRET_KEY`           | insecure dev key                 | Django secret key               |
| `DEBUG`                | `True`                           | Debug mode                      |
| `ALLOWED_HOSTS`        | `localhost,127.0.0.1`            | Comma-separated allowed hosts   |
| `DB_ENGINE`            | `django.db.backends.sqlite3`     | Database backend                |
| `DB_NAME`              | `db.sqlite3`                     | Database name / path            |
| `DB_USER`              | *(empty)*                        | Database user                   |
| `DB_PASSWORD`          | *(empty)*                        | Database password               |
| `DB_HOST`              | *(empty)*                        | Database host                   |
| `DB_PORT`              | *(empty)*                        | Database port                   |
| `CORS_ALLOWED_ORIGINS` | `http://localhost:5173`          | Allowed CORS origins            |

## Project Structure

```
subwatch-backend/
├── accounts/          # User-related app (empty scaffold for now)
├── subwatch_backend/  # Django project package
│   ├── settings.py    # Configured for DRF, JWT, CORS, env-driven DB
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
