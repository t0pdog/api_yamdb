### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/t0pdog/api_yamdb.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

По адресу ниже доступна документация в формате redoc:

```
http://127.0.0.1:8000/redoc/
```


Вот некоторые примеры запросов к эндпоинтам и их ответы:


Получение списка всех произведений
Получить список всех объектов.

Права доступа: Доступно без токена ( GET запрос):

```
http://127.0.0.1:8000/api/v1/titles/
```

Ответ сервера:
```
[{
"count": 0,
"next": "string",
"previous": "string",
"results": [
{
"id": 0,
"name": "string",
"year": 0,
"rating": 0,
"description": "string",
"genre": [
{
"name": "string",
"slug": "string"
}],
"category": {
"name": "string",
"slug": "string"
}}]}]
```


Получение информации о произведении
Информация о произведении

Права доступа: Доступно без токена ( GET запрос):


```
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```

Ответ сервера:
```
{
"id": 0,
"name": "string",
"year": 0,
"rating": 0,
"description": "string",
"genre": [
{
"name": "string",
"slug": "string"
}
],
"category": {
"name": "string",
"slug": "string"
}}
