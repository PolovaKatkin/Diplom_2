import random
import secrets

import allure
from faker import Faker
import json


@allure.step('Генерируем рандомный хэш для ингредиентов.')
def generate_random_hex_24():
    hex = secrets.token_hex(12)
    return hex


class GenerateRandomUser:
    # генерируем email, пароль и имя пользователя
    @staticmethod
    def generate_random_user_data():
        # генерируем логин, пароль и имя пользователя
        fake = Faker(locale="ru_RU")
        # собираем тело запроса
        payload = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()
        }
        return payload


class DataGenerationOrder:
    @staticmethod
    def generate_order_data(color):
        fake = Faker(locale="ru_RU")
        payload = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.address(),
            "metroStation": random.randrange(10),
            "phone": fake.phone_number(),
            "rentTime": random.randrange(6),
            "deliveryDate": fake.date(),
            "color": color,
            "comment": fake.text(10)
        }

        return json.dumps(payload)
