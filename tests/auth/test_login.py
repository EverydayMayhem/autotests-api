from http import HTTPStatus

import pytest

from clients.auth_client.auth_client import AuthClient
from clients.auth_client.auth_model import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.validate_json_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.auth
class TestLogin:
    def test_login(self,
                   public_auth_client: AuthClient,
                   function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)

        response = public_auth_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
