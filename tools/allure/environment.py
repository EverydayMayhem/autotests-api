from config import settings
from pydantic import FilePath

path = FilePath('./allure-result')
def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(path.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл