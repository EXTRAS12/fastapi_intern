# fastapi_intern

## Установка
Создайте clone:
```
git clone https://github.com/EXTRAS12/fastapi_intern.git
```

Создайте виртуальное окружение и запустите:
```
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости: 
```
pip install -r requirements.txt
```
Создайте файл .env:

Подключите базу данных
Пример:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fastapi_intern
DB_USER=postgres
DB_PASS=postgres
```

Сделайте миграцию:

```
alembic upgrade head
```
```
Перейдите в src и запустите python main.py 
```
```
Или uvicorn main:app --reload
```


