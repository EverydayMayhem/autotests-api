import pytest

from clients.auth_client.auth_client import get_auth_client, AuthClient


@pytest.fixture
def public_auth_client() -> AuthClient:
    return get_auth_client()
