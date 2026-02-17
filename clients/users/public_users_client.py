from httpx import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    Класс для работы с endpoint /users
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создает пользователя с заданными параметрами
        :param request: словарь с email, password, lastName, firstName, middleName
        :return: возвращает объект типа httpx.Response
        """
        return self.post(url='/api/v1/users', json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        обертка над create_user_api, которая возвращает сразу json
        :param request: UserRequestDict
        :return: CreateUserResponse
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
