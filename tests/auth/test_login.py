from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.auth_client.auth_client import AuthClient
from clients.auth_client.auth_model import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.validate_json_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.auth
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestLogin:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    @allure.title("Login with email and password")
    def test_login(self,
                   public_auth_client: AuthClient,
                   function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)

        response = public_auth_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
