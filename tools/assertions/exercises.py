from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_model import CreateExerciseRequestSchema, CreateExerciseResponseSchema, ExerciseSchema, \
    GetExercisesResponseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from tools.assertions.base import assert_equals, assert_length


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет соответствие запросу на создание задания и ответ
    :param request: запрос на создание задания
    :param response: ответ на создание задания
    """
    assert_equals(request.title, response.exercise.title, 'title')
    assert_equals(request.course_id, response.exercise.course_id, 'course_id')
    assert_equals(request.max_score, response.exercise.max_score, 'max_score')
    assert_equals(request.min_score, response.exercise.min_score, 'min_score')
    assert_equals(request.order_index, response.exercise.order_index, 'order_index')
    assert_equals(request.description, response.exercise.description, 'description')
    assert_equals(request.estimated_time, response.exercise.estimated_time, 'estimated_time')

def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет соответствие модели Задания
    :param actual: фактическая модель
    :param expected: ожидаемая модель
    """
    assert_equals(actual.id, expected.id, 'id')
    assert_equals(actual.title, expected.title, 'title')
    assert_equals(actual.course_id, expected.course_id, 'course_id')
    assert_equals(actual.max_score, expected.max_score, 'max_score')
    assert_equals(actual.min_score, expected.min_score, 'min_score')
    assert_equals(actual.order_index, expected.order_index, 'order_index')
    assert_equals(actual.description, expected.description, 'description')
    assert_equals(actual.estimated_time, expected.estimated_time, 'estimated_time')

def assert_get_exercise_response(get_exercise_response: GetExerciseResponseSchema,
                                 create_exercise_response: CreateExerciseResponseSchema):
    """
    Сравнение ответа на получение занятия и ответа на создание этого занятия

    :param get_exercise_response: запрос на получение занятия
    :param create_exercise_response: ответ на получение занятия
    """
    assert_exercise(get_exercise_response.exercise, create_exercise_response.exercise)

def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Метод сравнения запроса на обновление занятия и ответа
    :param request: запрос на обновление занятия
    :param response: ответ на обновление занятия
    :return:
    """
    if request.title:
        assert_equals(request.title, response.exercise.title, 'title')

    if request.description:
        assert_equals(request.description, response.exercise.description, 'description')

    if request.min_score:
        assert_equals(request.min_score, response.exercise.min_score, 'min_score')

    if request.max_score:
        assert_equals(request.max_score, response.exercise.max_score, 'max_score')

    if request.estimated_time:
        assert_equals(request.estimated_time, response.exercise.estimated_time, 'estimated_time')

    if request.order_index:
        assert_equals(request.order_index, response.exercise.order_index, 'order_index')

def assert_internal_error_response(
        actual: InternalErrorResponseSchema,
        expected: InternalErrorResponseSchema
):
    """
    Функция для проверки внутренней ошибки. Например, ошибки 404 (File not found).

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equals(actual.details, expected.details, "details")

def assert_exercise_not_found_error(actual: InternalErrorResponseSchema):
    """
    Функция для проверки 404 ошибки - не найдено занятие

    :param actual: InternalErrorResponseSchema
    """
    expected = InternalErrorResponseSchema(detail="Exercise not found")
    assert_internal_error_response(actual, expected)

def assert_get_exercises_response(get_exercises_response: GetExercisesResponseSchema,
                                  create_exercises_response: list[CreateExerciseResponseSchema]):
    """
    Функция проверяет, что запрос на получение всех занятий курса равен ответу на создание этих занятий

    :param get_exercises_response: GetExercisesResponseSchema
    :param create_exercises_response: список CreateExerciseResponseSchema
    """
    assert_length(get_exercises_response.exercises, create_exercises_response, 'exercises')

    for index, create_exercise_response in enumerate(create_exercises_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercise_response.exercise)