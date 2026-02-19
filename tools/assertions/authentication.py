from tools.assertions.base import assert_is_true, assert_equals
from clients.auth_client.auth_model import LoginResponseSchema


def assert_login_response(response: LoginResponseSchema):
    """
    Сравнение ответа на аутентификацию

    :param response: ответ
    """
    assert_equals(response.token.token_type, 'bearer', 'Token type')
    assert_is_true(response.token.access_token, 'access_token')
    assert_is_true(response.token.refresh_token, 'refresh_token')


