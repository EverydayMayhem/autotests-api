import pytest
from pydantic import BaseModel, EmailStr

from clients.users.private_users_client import PrivateUsersClient, AuthenticationUserSchema, get_private_users_client
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        """
        Данные для авторизации пользователя в виде AuthenticationUserSchema
        :return:
        """
        return AuthenticationUserSchema(email=self.email, password=self.password)

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
def private_user_client(function_user: UserFixture) -> PrivateUsersClient:
    private_client = get_private_users_client(function_user.authentication_user)
    return private_client


@pytest.fixture
def function_user(public_user_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_user_client.create_user(request)
    return UserFixture(request=request, response=response)
