import allure
import pytest
from faker import Faker

from stellar_burgers_api import MethodsUser


@allure.story("Ручка /api/auth/user")
@allure.description("Получение и обновление информации о пользователе")
class TestUpdateUser:
    fake = Faker(locale="ru_RU")

    @allure.description('Проверка успешного изменения данных о пользователя, когда пользователь авторизован.')
    @pytest.mark.parametrize('update_data', [({'email': fake.email()}),
                                             ({'password': fake.password()}),
                                             ({'name': fake.name()})])
    def test_update_user_with_login_success(self, register_user_login_and_delete, update_data):

        token = register_user_login_and_delete[2]
        update_user = MethodsUser.update_user(token, update_data)

        assert (
                update_user.status_code == 200 and
                update_user.json()['success'] is True
        )

    @allure.description('Проверка невозможности изменения данных о пользователе, когда пользователь не авторизован.')
    @pytest.mark.parametrize('update_data', [({'email': fake.email()}),
                                             ({'password': fake.password()}),
                                             ({'name': fake.name()})])
    def test_update_user_with_login_success(self, update_data):
        update_user = MethodsUser.update_user(token_user='', payload=update_data)

        assert (
                update_user.status_code == 401 and
                update_user.json()["message"] == "You should be authorised"
        )
