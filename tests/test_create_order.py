import allure
from handlers.handlers import post_user_order


@allure.epic("HTTP")
@allure.feature("api/orders")
@allure.suite('Проверка ручки создания заказа')
class TestChangeUserDatar:

    @allure.title(f'Создаем заказ с авторизацией')
    def test_create_order_with_authorised_user_and_ingredients(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(
            body={'ingredients': ["61c0c5a71d1f82001bdaaa6d"]},
            headers={'Authorization': register_new_user_and_login}
        )
        assert response.ok
        assert response.json()['name'] == 'Флюоресцентный бургер'

    @allure.title(f'Создаем заказ без авторизации')
    def test_create_order_with_not_authorised_user_and_ingredients(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(body={'ingredients': ["61c0c5a71d1f82001bdaaa6d"]}, headers={})
        assert response.ok
        assert response.json()['name'] == 'Флюоресцентный бургер'

    @allure.title(f'Создаем заказ с авторизацией без ингредиента')
    def test_create_order_with_authorised_user_and_no_ingredients(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(body={'ingredients': []}, headers={'Authorization': register_new_user_and_login})
        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title(f'Создаем заказ без авторизации без ингредиента')
    def test_create_order_with_not_authorised_user_and_no_ingredients(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(body={'ingredients': []}, headers={})
        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title(f'Создаем заказ с авторизацией с неверным ингридиентом')
    def test_create_order_with_authorised_user_and_incorrect_ingredient(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(
            body={'ingredients': ["61c0c5a711d1f82001bdaaa6d"]},
            headers={'Authorization': register_new_user_and_login}
        )
        assert response.status_code == 500
        assert response.reason == 'Internal Server Error'

    @allure.title(f'Создаем заказ без авторизации с неверным ингридиентом')
    def test_create_order_with_not_authorised_user_and_incorrect_ingredient(
            self,
            register_new_user_and_login: str
    ):
        response = post_user_order(body={'ingredients': ["61c0c5a71d11f82001bdaaa6d"]}, headers={})
        assert response.status_code == 500
        assert response.reason == 'Internal Server Error'
