import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_model import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CoursesFixture
from fixtures.users import UserFixture


class ExercisesFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema

    @property
    def exercise_id(self):
        return self.response.exercise.id


@pytest.fixture
def exercise_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercises_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(function_courses: CoursesFixture,
                      exercise_client: ExercisesClient
                      ) -> ExercisesFixture:
    request = CreateExerciseRequestSchema(course_id=function_courses.course_id)
    response = exercise_client.create_exercise(request)
    return ExercisesFixture(request=request, response=response)
