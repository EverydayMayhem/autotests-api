import pytest

from pydantic import BaseModel, EmailStr

from clients.auth_client.auth_client import get_auth_client, AuthClient
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password


@pytest.fixture
def public_user_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def public_auth_client() -> AuthClient:
    return get_auth_client()

@pytest.fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request=request, response=response)
