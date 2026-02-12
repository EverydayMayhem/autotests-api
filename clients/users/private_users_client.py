from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class User(TypedDict):
    """
    Описание структуры пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class GetUserResponse(TypedDict):
    """
    Описание ответа на получение пользователя
    """
    user: User

class UpdateUserRequestDict(TypedDict):
    """
    Описание структуры request для patch_user_api
    """
    email: str | None
    lastName: str | None
    firstName: str | None
    middleName: str | None


class PrivateUsersClient(APIClient):
    """
    Класс для работы с приватными эндпоинтами /api/v1/users/
    """

    def get_user_me_api(self) -> Response:
        """
        Метод получения текущего пользователя.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url='/api/v1/users/me')

    def get_user_api(self, user_id: str) -> Response:
        """
        Метод получения пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f'/api/v1/users/{user_id}')

    def patch_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/users/{user_id}', json=request)

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponse:
        """
        Метод получения тела ответа get_user_api
        :param user_id: идентификатор пользователя
        :return: возвращает объект GetUserResponseDict
        """
        response = self.get_user_api(user_id)
        return response.json()

def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))
