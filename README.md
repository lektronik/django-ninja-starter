# Django Ninja Boilerplate ("NinjaStart")
**Status**: Ready for Cloning

## Description
A production-ready foundation for building high-performance APIs with Django 5.0 and Django Ninja.

## Features
- Domain-Driven Design structure (`features/`).
- JWT Authentication (`ninja-jwt`).
- Docker support.

## How to Use
```bash
# Clone this to start a new project
cp -r django-ninja-starter my-new-api
cd my-new-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
