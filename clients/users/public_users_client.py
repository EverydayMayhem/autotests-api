from httpx import Response

import allure
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema
from tools.routes import APIRoutes
from clients.api_coverage import tracker

class PublicUsersClient(APIClient):
    """
    Класс для работы с endpoint /users
    """

    @allure.step("Create user")
    @tracker.track_coverage_httpx(APIRoutes.USERS)
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Метод создает пользователя с заданными параметрами
        :param request: словарь с email, password, lastName, firstName, middleName
        :return: возвращает объект типа httpx.Response
        """
        return self.post(url=APIRoutes.USERS, json=request.model_dump(by_alias=True))

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
