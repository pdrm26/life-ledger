makemigrations:
	@python manage.py makemigrations

migrate: makemigrations
	@python manage.py migrate

run:
	@python manage.py runserver


AMOUNT ?= 0
TEXT ?= ""
TOKEN ?= "your_secret_token"


expense:
	@curl -X POST -H token=$(TOKEN) --data "amount=$(AMOUNT)&text=$(TEXT)" http://localhost:8000/finance/submit/expense

income:
	@curl -X POST -H token=$(TOKEN) --data "amount=$(AMOUNT)&text=$(TEXT)" http://localhost:8000/finance/submit/income