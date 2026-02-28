from http import HTTPStatus

import allure
import pytest
from allure_commons.types import Severity

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_model import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExerciseQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.exercises import ExercisesFixture
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTags
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_error, assert_get_exercises_response
from tools.assertions.validate_json_schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
@allure.tag(AllureTags.EXERCISES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.EXERCISES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.EXERCISES)
class TestExercises:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    @allure.title("Create exercise")
    def test_create_exercise(self,
                             exercise_client: ExercisesClient,
                             function_courses: CoursesFixture):
        request = CreateExerciseRequestSchema(course_id=function_courses.course_id)
        response = exercise_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.title("Get exercise")
    def test_get_exercise(self,
                          exercise_client: ExercisesClient,
                          function_exercise: ExercisesFixture):
        response = exercise_client.get_exercise_api(function_exercise.exercise_id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.CRITICAL)
    @allure.story(AllureStory.UPDATE_ENTITY)
    @allure.sub_suite(AllureStory.UPDATE_ENTITY)
    @allure.title("Update exercise")
    def test_update_exercise(self,
                             exercise_client: ExercisesClient,
                             function_exercise: ExercisesFixture
                             ):
        request = UpdateExerciseRequestSchema()
        response = exercise_client.update_exercise_api(function_exercise.exercise_id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.DELETE_ENTITY)
    @allure.sub_suite(AllureStory.DELETE_ENTITY)
    @allure.title("Delete exercise")
    def test_delete_exercise(self,
                             function_exercise: ExercisesFixture,
                             exercise_client: ExercisesClient):
        response_delete = exercise_client.delete_exercise_api(function_exercise.exercise_id)

        assert_status_code(response_delete.status_code, HTTPStatus.OK)

        response_get = exercise_client.get_exercise_api(function_exercise.exercise_id)
        response_get_data = InternalErrorResponseSchema.model_validate_json(response_get.text)

        assert_status_code(response_get.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_error(response_get_data)

        validate_json_schema(response_get.json(), response_get_data.model_json_schema())

    @allure.severity(Severity.NORMAL)
    @allure.story(AllureStory.GET_ENTITIES)
    @allure.sub_suite(AllureStory.GET_ENTITIES)
    @allure.title("Get all exercises")
    def test_get_all_exercises(self,
                               function_courses: CoursesFixture,
                               function_exercise: ExercisesFixture,
                               exercise_client: ExercisesClient):
        request = GetExerciseQuerySchema(course_id=function_courses.course_id)
        response = exercise_client.get_exercises_api(request)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercises_response(response_data, [function_exercise.response])

        validate_json_schema(response.json(), response_data.model_json_schema())