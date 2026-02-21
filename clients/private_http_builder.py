from httpx import Client

from pydantic import BaseModel, EmailStr
from clients.auth_client.auth_client import get_auth_client
from clients.auth_client.auth_model import LoginRequestSchema


class AuthenticationUserSchema(BaseModel):
    """
    Класс для аннотирования полей AuthUser
    """
    email: EmailStr
    password: str


def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    auth_client = get_auth_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestSchema(email=user.email, password=user.password)

    # Выполняем POST запрос и аутентифицируемся
    login_response = auth_client.login(login_request)

    return Client(
        timeout=100,
        base_url='http://localhost:8000',
        headers={'Authorization': f'Bearer {login_response.token.access_token}'}
    )
