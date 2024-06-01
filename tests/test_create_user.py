import allure
import pytest

from helpers import GenerateRandomUser
from stellar_burgers_api import MethodsUser


@allure.story("Ручка /api/auth/register")
@allure.description("Создание/регистрация пользователя")
class TestCreateUser:
    @allure.description("Создание пользователя с корректными данными. "
                        "Получаем код 200 и тело ответа в котором есть: 'success':true")
    def test_create_uniq_user_success(self, generate_user_data_and_delete):
        data = generate_user_data_and_delete
        response = MethodsUser.create_user(data)

        assert (response.status_code == 200 and
                response.json()["success"] is True)

    @allure.description("Проверка невозможности создании пользователя, когда он уже зарегистрирован."
                        "Получаем ошибку 403")
    def test_create_double_user_return_status_code_403(self, register_user_login_and_delete):
        data = register_user_login_and_delete[0]
        response = MethodsUser.create_user(data)

        assert (response.status_code == 403 and
                response.json()["message"] == "User already exists")

    @allure.description("Проверка невозможности создании пользователя, когда одно из полей незаполненно."
                        "Получаем ошибку 403")
    @pytest.mark.parametrize('field', ['email', 'password'])
    def test_create_user_with_empty_field_error(self, field):
        user_data = GenerateRandomUser.generate_random_user_data()
        payload = user_data
        payload.pop(field)
        response = MethodsUser.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"

