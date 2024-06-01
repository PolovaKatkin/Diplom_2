import allure
import pytest

from helpers import GenerateRandomUser
from stellar_burgers_api import MethodsUser


@allure.step('Создаем данные для пользователя, передаем их, после теста удаляем его.')
@pytest.fixture(scope='function')
def generate_user_data_and_delete():
    data_payload = GenerateRandomUser.generate_random_user_data()
    yield data_payload

    login = MethodsUser.login_user(data_payload)
    token_user = login.json()['accessToken']
    MethodsUser.delete_user(token_user)


@allure.step('Регистрируем пользователя, логинимся, после теста удаляем его.')
@pytest.fixture(scope='function')
def register_user_login_and_delete():
    data_payload = GenerateRandomUser.generate_random_user_data()
    login = MethodsUser.create_and_login_user(data_payload)
    token_user = login.json()['accessToken']
    yield data_payload, login, token_user

    MethodsUser.delete_user(token_user)
