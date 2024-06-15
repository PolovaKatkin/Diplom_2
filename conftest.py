import allure
import pytest

from helpers import GenerateRandomUser
from stellar_burgers_api import MethodsUser


@allure.step('Создаем данные для пользователя, передаем их, после теста удаляем его.')
@pytest.fixture(scope='function')
def create_user():
    data_payload = GenerateRandomUser.generate_random_user_data()
    response = MethodsUser.create_user(data_payload)
    yield data_payload, response


@allure.step('Логинимся под пользователем и получаем токен.')
@pytest.fixture(scope='function')
def token(create_user):
    data_payload = create_user[0]
    login = MethodsUser.login_user(data_payload)
    token = login.json()['accessToken']
    return token, login


@allure.step('Удаляем пользователя после теста.')
@pytest.fixture(scope='function')
def delete_user(token):
    yield
    MethodsUser.delete_user(token[0])


@allure.step('Создаем пользователя, логинимся и удаляем после теста.')
@pytest.fixture(scope='function')
def login_user(create_user, token, delete_user):
    data_payload = create_user[0]
    login = token[1]
    token_user = token[0]
    yield data_payload, login, token_user
