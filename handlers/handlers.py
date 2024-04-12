import allure
import requests


@allure.step(f'Дергаем ручку auth/register')
def post_register_user(body: dict):
    return requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json=body)


@allure.step(f'Дергаем ручку auth/login')
def post_login_user(body: dict):
    return requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', json=body)


@allure.step(f'Дергаем ручку auth/user')
def patch_user_info(body: dict, headers: dict):
    return requests.patch('https://stellarburgers.nomoreparties.site/api/auth/user', data=body, headers=headers)


@allure.step(f'Дергаем ручку api/orders')
def post_user_order(body: dict, headers: dict):
    return requests.post('https://stellarburgers.nomoreparties.site/api/orders', data=body, headers=headers)


@allure.step(f'Дергаем ручку api/orders')
def get_user_order(headers: dict):
    return requests.get('https://stellarburgers.nomoreparties.site/api/orders', headers=headers)


@allure.step(f'Дергаем ручку api/ingredients')
def get_ingridients(body: dict):
    return requests.get('https://stellarburgers.nomoreparties.site/api/ingredients', data=body)


@allure.step(f'Дергаем ручку auth/logout')
def post_logout(body: dict):
    return requests.post('https://stellarburgers.nomoreparties.site/api/auth/logout', data=body)
