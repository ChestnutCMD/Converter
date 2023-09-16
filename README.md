# Converter

Задание:
Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
GET /api/rates?from=USD&to=RUB&value=1
Ответ:
{

"result": 62.16

}

# docker
<p>docker pull cheshtnut/converter:v1.0</p>
<p>docker container run -d -p 4000:5000 cheshtnut/converter:v1.0</p>
