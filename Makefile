.PHONY: run migrate install clean

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations features
	python manage.py migrate

install:
	pip install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
