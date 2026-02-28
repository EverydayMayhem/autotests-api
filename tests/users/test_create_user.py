from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_model import CreateUserRequestSchema, CreateUserResponseSchema
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.users import assert_create_user_response
from tools.assertions.validate_json_schema import validate_json_schema
from tools.fakers import fake


@pytest.mark.regression
@pytest.mark.users
@pytest.mark.parametrize('domain', ['mail.ru', 'gmail.com', 'example.com'])
@allure.tag(AllureTags.USERS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestCreateUser:
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self,
                         public_user_client: PublicUsersClient,
                         domain: str):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_user_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
