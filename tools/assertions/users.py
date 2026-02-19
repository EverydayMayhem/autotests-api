from tools.assertions.base import assert_equals

from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema

def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equals(response.user.email, request.email, 'email')
    assert_equals(response.user.first_name, request.first_name, 'first_name')
    assert_equals(response.user.last_name, request.last_name, 'last_name')
    assert_equals(response.user.middle_name, request.middle_name, 'middle_name')