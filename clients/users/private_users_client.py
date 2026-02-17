from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.users_model import GetUserResponseSchema, UpdateUserRequestSchema



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

    def patch_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        """
        Метод обновления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :param request: Словарь с email, lastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f'/api/v1/users/{user_id}', json=request.model_dump(by_alias=True))

    def delete_user_api(self, user_id: str) -> Response:
        """
        Метод удаления пользователя по идентификатору.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f'/api/v1/users/{user_id}')

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Метод получения тела ответа get_user_api
        :param user_id: идентификатор пользователя
        :return: возвращает объект GetUserResponseDict
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса PrivateUsersClient
    """
    return PrivateUsersClient(client=get_private_http_client(user))
