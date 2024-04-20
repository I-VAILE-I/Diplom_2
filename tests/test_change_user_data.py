import allure
from handlers.handlers import patch_user_info


@allure.epic("HTTP")
@allure.feature("auth/user")
@allure.suite('Проверка ручки изменения информации о пользователе')
class TestChangeUserDatar:

    @allure.title(f'Проверяем смену имени для авторизированного пользователя')
    def test_change_user_name_for_authorised_user(
            self,
            register_new_user_and_login: str
    ):
        response = patch_user_info(
            body={'name': 'qa_test_andrew_5'},
            headers={'Authorization': register_new_user_and_login}
        )
        assert response.ok
        assert response.json()['user']['name'] == 'qa_test_andrew_5'

    @allure.title(f'Проверяем смену почты для не авторизированного пользователя')
    def test_change_user_email_for_authorised_user(
            self,
            register_new_user_and_login: str,
            return_login_password: dict
    ):
        response = patch_user_info(
            body={'email': return_login_password['email']},
            headers={'Authorization': register_new_user_and_login}
        )
        assert response.ok
        assert response.json()['user']['email'] == return_login_password['email']

    @allure.title(f'Проверяем смену имени для не авторизированного пользователя ')
    def test_change_user_name_for_not_authorised_user(
            self,
            register_new_user_and_login: str
    ):
        response = patch_user_info(body={'name': 'qa_test_andrew_5'}, headers={})
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'

    @allure.title(f'Проверяем смену почты для не авторизированного пользователя')
    def test_change_user_email_for_not_authorised_user(
            self,
            register_new_user_and_login: str,
            return_login_password: dict
    ):
        response = patch_user_info(body={'email': return_login_password['email']}, headers={})
        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
