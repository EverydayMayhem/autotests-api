from tools.assertions.base import assert_equals

from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema


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

def assert_users(actual: UserSchema, expected: UserSchema):
    """
    Проверяет пользователя в запросе и ответе

    :param actual:
    :param expected:
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equals(expected.id, actual.id, 'id')
    assert_equals(expected.email, actual.email, 'email')
    assert_equals(expected.first_name, actual.first_name, 'first_name')
    assert_equals(expected.last_name, actual.last_name, 'last_name')
    assert_equals(expected.middle_name, actual.middle_name, 'middle_name')

def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет ответ создания пользователя и получения пользователя
    :param create_user_response:
    :param get_user_response:
    :param actual:
    :param expected:
    :return:
    """
    assert_users(actual=get_user_response.user, expected=create_user_response.user)