import allure
from handlers.handlers import post_login_user


@allure.epic("HTTP")
@allure.feature("auth/login")
@allure.suite('Проверка ручки логина пользователя')
class TestLoginUser:

    @allure.title(f'Проверяем логина пользователя')
    def test_login_registered_user(
            self,
            register_new_user_and_return_login_password: dict
    ):
        body = {
            "email": register_new_user_and_return_login_password["email"],
            "password": register_new_user_and_return_login_password["password"]
        }
        response = post_login_user(body=body)

        assert response.ok
        assert response.json()['success']

    @allure.title(f'Проверяем логина пользователя')
    def test_login_registered_user_with_incorrect_password(
            self,
            register_new_user_and_return_login_password: dict
    ):
        body = {
            "email": register_new_user_and_return_login_password["email"],
            "password": f'{register_new_user_and_return_login_password["password"]}123'
        }
        response = post_login_user(body=body)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
