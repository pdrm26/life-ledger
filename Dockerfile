FROM python:3.11.4-alpine


ENV PYTHONUNBUFFERD=TRUE
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
