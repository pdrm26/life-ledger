makemigrations:
	@python manage.py makemigrations

migrate: makemigrations
	@python manage.py migrate

run:
	@python manage.py runserver

shell:
	@python manage.py shell

ruff:
	ruff check --fix
