import allure
import random
import string


@allure.step(f'Генерация даннях для создания курьера')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string
