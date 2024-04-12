import allure
from handlers.handlers import post_user_order, get_user_order


@allure.epic("HTTP")
@allure.feature("api/orders")
@allure.suite('Проверка ручки получения заказов пользователя')
class TestChangeUserDatar:

    @allure.title(f'Получаем информацию о заказе с авторизорованным пользователем')
    def test_get_order_with_authorised_user(
            self,
            register_new_user_and_login: str
    ):
        post_user_order(
            body={'ingredients': ["61c0c5a71d1f82001bdaaa6d"]},
            headers={'Authorization': register_new_user_and_login})
        response = get_user_order(headers={'Authorization': register_new_user_and_login})
        assert response.ok
        assert response.json()['orders'][0]['name'] == 'Флюоресцентный бургер'

    @allure.title(f'Получаем информацию о заказе с не авторизорованным пользователем')
    def test_get_order_with_not_authorised_user(
            self,
            register_new_user_and_login: str
    ):
        post_user_order(
            body={'ingredients': ["61c0c5a71d1f82001bdaaa6d"]},
            headers={'Authorization': register_new_user_and_login})
        response = get_user_order(headers={})
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'