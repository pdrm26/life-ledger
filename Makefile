makemigrations:
	@python manage.py makemigrations

migrate: makemigrations
	@python manage.py migrate

run:
	@python manage.py runserver