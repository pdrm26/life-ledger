makemigrations:
	@python manage.py makemigrations

migrate: makemigrations
	@python manage.py migrate

runserver:
	@python manage.py runserver