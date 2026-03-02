# 🚀 Django Ninja Starter

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Django 5.0](https://img.shields.io/badge/django-5.0-092E20.svg)](https://www.djangoproject.com/)

A production-ready boilerplate for building high-performance APIs with **Django 5.0** and **Django Ninja**. Skip the setup and start building features immediately.

## ✨ What's Included

- **Django Ninja** — Fast, async-ready API framework with automatic OpenAPI docs
- **JWT Authentication** — Token-based auth via `ninja-jwt` (access + refresh tokens)
- **Domain-Driven Structure** — Feature-based layout (`features/`) instead of flat apps
- **Docker Support** — Ready-to-use `Dockerfile` and `docker-compose.yml` with PostgreSQL
- **CI Pipeline** — GitHub Actions workflow for automated testing (`test.yml`)
- **Code Quality** — Pre-configured `pre-commit` hooks (Black, Flake8, syntax checks)
- **Security Hardening** — CSRF, HSTS, SSL redirect, secure cookies (auto-enabled in production)
- **CORS Configuration** — Pre-configured `django-cors-headers` with environment-aware defaults
- **Health Check** — Built-in `/api/health` endpoint for monitoring
- **Testing Setup** — `pytest` + `pytest-django` configured and ready
- **Makefile** — Common commands (`make run`, `make migrate`, `make install`)
- **Environment Variables** — `.env` support via `python-dotenv`

## 📁 Project Structure

```
django-ninja-starter/
├── app/                    # Core Django project
│   ├── api.py              # NinjaExtraAPI instance & router registration
│   ├── auth.py             # JWT authentication utilities
│   ├── settings.py         # Django settings (security-hardened)
│   └── urls.py             # URL configuration
├── features/               # Domain-driven feature modules
│   ├── auth/               # User registration & auth endpoints
│   ├── products/           # Product management
│   ├── cart/               # Shopping cart
│   ├── orders/             # Order processing
│   ├── api.py              # Feature routers
│   ├── models.py           # Database models
│   ├── schemas.py          # Pydantic schemas
│   └── tests.py            # Test suite
├── .env.example            # Environment variable template
├── .gitignore
├── LICENSE
├── Makefile
├── manage.py
├── pytest.ini
├── requirements.txt
├── SECURITY.md
└── CONTRIBUTING.md
```

## 🚀 Quick Start

### Option 1: Using Docker (Recommended)

```bash
# Clone the boilerplate
git clone https://github.com/lektronik/django-ninja-starter.git
cd django-ninja-starter

# Configure environment
cp .env.example .env

# Build and run with PostgreSQL
docker-compose up --build
```

### Option 2: Local Setup

```bash
# Set up environment
python3 -m venv venv
source venv/bin/activate
make install

# Configure environment
cp .env.example .env

# Setup pre-commit hooks
pre-commit install

# Run migrations and start
make migrate
make run
```

API docs are automatically available at **http://localhost:8000/api/docs**

## 🔐 Security

This boilerplate includes production security defaults that activate automatically when `DEBUG=False`:

| Setting | Development | Production |
|---|---|---|
| `CSRF_COOKIE_SECURE` | `False` | `True` |
| `SESSION_COOKIE_SECURE` | `False` | `True` |
| `SECURE_SSL_REDIRECT` | `False` | `True` |
| `SECURE_HSTS_SECONDS` | `0` | `31536000` (1 year) |
| `SECURE_HSTS_PRELOAD` | `False` | `True` |
| `CORS_ALLOW_ALL_ORIGINS` | `True` | `False` |

See [SECURITY.md](SECURITY.md) for the full security policy.

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

## 🛠 API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `GET` | `/api/health` | Public | Health check |
| `POST` | `/api/token/pair` | Public | Obtain JWT tokens |
| `POST` | `/api/token/refresh` | Public | Refresh access token |
| `POST` | `/api/auth/register` | Public | User registration |
| `GET` | `/api/products/` | Public | List products |
| `GET` | `/api/products/{id}` | Public | Get product detail |
| `GET` | `/api/cart/` | Required | View cart |
| `POST` | `/api/cart/add` | Required | Add item to cart |

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `Django 5.0` | Web framework |
| `django-ninja` | API framework |
| `ninja-jwt` | JWT authentication |
| `django-cors-headers` | CORS middleware |
| `python-dotenv` | Environment variables |
| `psycopg2-binary` | PostgreSQL driver |
| `pytest` / `pytest-django` | Testing |

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
