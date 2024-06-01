import allure

from helpers import generate_random_hex_24
from stellar_burgers_api import MethodsOrder


@allure.story("Ручка /api/orders")
@allure.description("Создание заказа")
class TestCreateOrder:
    @allure.description("Проверка создания заказа c ингредиентами авторизованным пользователем. "
                        "Получаем код 200 и тело ответа в котором есть: 'success':true")
    def test_create_order_with_auth_with_ingredients_success(self, register_user_login_and_delete):
        ingredients = MethodsOrder.get_ingredients()
        token = register_user_login_and_delete[2]
        order_response = MethodsOrder.create_order(token_user=token, ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )
        pass

    @allure.description("Проверка создания заказа c ингредиентами не авторизованным пользователем. "
                        "Получаем код 200 и тело ответа в котором есть: 'success':true")
    def test_create_order_without_auth_with_ingredients_success(self):
        ingredients = MethodsOrder.get_ingredients()
        order_response = MethodsOrder.create_order(token_user='', ids=ingredients)
        assert (
                order_response.status_code == 200
                and order_response.json()['success'] is True
        )

    @allure.description("Проверка создания заказа без ингредиентов авторизованным пользователем. "
                        "Получаем код 400 и тело ответа в котором есть: 'success':false")
    def test_create_order_with_auth_without_ingredients_error(self, register_user_login_and_delete):
        token = register_user_login_and_delete[2]
        order_response = MethodsOrder.create_order(token_user=token, ids='')
        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
        )

    @allure.description("Проверка создания заказа без ингредиентов не авторизованным пользователем. "
                        "Получаем код 400 и тело ответа в котором есть: 'success':false")
    def test_create_order_without_auth_without_ingredients_error(self, register_user_login_and_delete):
        order_response = MethodsOrder.create_order(token_user='', ids='')
        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
        )

    @allure.description("Проверка создания заказа с неверным хешем ингредиентов. "
                        "Получаем код 400")
    # Примечание: в документации указан код 500, видимо утсаревшая документация
    def test_create_order_with_incorrect_hex_error_400(self):
        ingredients = generate_random_hex_24()
        order_response = MethodsOrder.create_order(token_user='', ids=ingredients)

        assert (
                order_response.status_code == 400 and
                order_response.text == '{"success":false,"message":"One or more ids provided are incorrect"}'
        )
