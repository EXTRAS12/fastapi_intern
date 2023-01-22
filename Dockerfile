FROM python:3.10-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /temp/requirements.txt

WORKDIR /app

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r /temp/requirements.txt
