import allure
import pytest

from handlers.handlers import post_register_user, post_logout
from helpers import generate_random_string


@pytest.fixture(scope="function")
@allure.step(f'Подготавливаем словарь с данными для создания курьера')
def generate_and_return_login_password():
    login_pass = {
        "email": f'{generate_random_string(10)}@yandex.ru',
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }
    return login_pass


@pytest.fixture(scope="function")
@allure.step(f'Регистрация пользователя и выход из системы')
def register_new_user_and_return_login_password_and_logout():
    body = {
        "email": f'{generate_random_string(10)}@yandex.ru',
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }

    response = post_register_user(body=body)
    post_logout(body={'token': response.json()['refreshToken']})

    if response.status_code == 200:
         return body


@pytest.fixture(scope="function")
@allure.step(f'Регистрация пользователя')
def register_new_user_and_return_login_password():
    body = {
        "email": f'{generate_random_string(10)}@yandex.ru',
        "password": generate_random_string(10),
        "name": generate_random_string(10),
    }

    response = post_register_user(body=body)

    if response.status_code == 200:
         return body
