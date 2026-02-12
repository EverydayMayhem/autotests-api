from httpx import Response
from typing_extensions import TypedDict

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class UserRequestDict(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Класс для работы с endpoint /users
    """
    def create_user_api(self, request: UserRequestDict) -> Response:
        """
        Метод создает пользователя с заданными параметрами
        :param request: словарь с email, password, lastName, firstName, middleName
        :return: возвращает объект типа httpx.Response
        """
        return self.post(url='/api/v1/users', json=request)

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())