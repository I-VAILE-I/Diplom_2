import allure
from handlers.handlers import post_register_user


@allure.epic("HTTP")
@allure.feature("auth/register")
@allure.suite('Проверка ручки регистрацию пользователя')
class TestCreatingUser:

    @allure.title(f'Проверяем регистрацию пользователя')
    def test_register_new_user(
            self,
            return_login_password: dict
    ):
        body = {
            "email": return_login_password["email"],
            "password": return_login_password["password"],
            "name": return_login_password["name"]
        }
        response = post_register_user(body=body)

        assert response.ok
        assert response.json()['success']

    @allure.title(f'Проверяем регистрацию уже зарегестрированного пользователя')
    def test_error_register_alredy_registered_user(
            self,
            register_new_user_and_return_login_password: dict
    ):
        response = post_register_user(body=register_new_user_and_return_login_password)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title(f'Проверяем регистрацию пользователя с пустым важным полем')
    def test_error_register_new_user_with_null_password(
            self,
            return_login_password: dict
    ):
        body = {
            "email": return_login_password["email"],
            "password": None,
            "name": return_login_password["name"]
        }
        response = post_register_user(body=body)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
