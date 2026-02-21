from http import HTTPStatus
import pytest
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
from tools.assertions.validate_json_schema import validate_json_schema

@pytest.mark.regression
@pytest.mark.users
def test_create_user(public_user_client: PublicUsersClient):
    request = CreateUserRequestSchema()
    response = public_user_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    assert_create_user_response(request, response_data)
    validate_json_schema(response.json(), response_data.model_json_schema())
