import allure
import pytest

from handlers.handlers import post_register_user, post_logout, post_login_user
from helpers import generate_random_string


@pytest.fixture(scope="function")
@allure.step(f'Подготавливаем словарь с данными для создания курьера')
def return_login_password():
    login_pass = {
        "email": f'{generate_random_string(10)}@yandex.ru',
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }
    return login_pass


@pytest.fixture(scope="function")
@allure.step(f'Регистрация пользователя и авторизация')
def register_new_user_and_login(return_login_password):
    body_on_register = return_login_password
    body_on_login = {
        "email": body_on_register['email'],
        "password": body_on_register['password']
    }

    register_response = post_register_user(body=body_on_register)

    if register_response.status_code == 200:
         return post_login_user(body=body_on_login).json()['accessToken']


@pytest.fixture(scope="function")
@allure.step(f'Регистрация пользователя')
def register_new_user_and_return_login_password(return_login_password):
    body = return_login_password

    response = post_register_user(body=body)

    if response.status_code == 200:
         return body
