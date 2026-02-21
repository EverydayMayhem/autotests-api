import pytest

from http import HTTPStatus

from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_model import GetUserResponseSchema
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.validate_json_schema import validate_json_schema
from tools.assertions.users import assert_get_user_response

@pytest.mark.regression
@pytest.mark.users
def test_user_me(private_user_client: PrivateUsersClient, function_user: UserFixture):
    response = private_user_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_get_user_response(response_data, function_user.response)
    validate_json_schema(response.json(), response_data.model_json_schema())

