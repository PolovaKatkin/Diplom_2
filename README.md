## Дипломный проект. Задание 2: API

### Автотесты для проверки API сайта Stellar Burgers https://stellarburgers.nomoreparties.site/

Реализованы проверки эндпоинтов:
* `POST /api/auth/register` - создание/регистрация пользователя
* `POST /api/auth/login` - авторизация пользователя
* `PATCH /api/auth/user` - получение и обновление информации о пользователе
* `POST /api/orders` - cоздание заказа
* `GET /api/orders` - получить заказы конкретного пользователя

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по эндпоинтам
- `conftest.py` - фикстуры
- `helpers.py` - файл с вспомогательными функциями
- `README.md` - описание проекта
- `requirements` - файл с необходимыми библиотеками
- `stellar_burgers_api.py` - файл с методами, вызываемыми в ходе тестов 
- `urls.py` - файл c URL

### Запуск автотестов

**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании в Allure**

> `pytest--alluredir=allure_results`

**Генерация отчета в html страницу**

>`allure serve allure_results`
