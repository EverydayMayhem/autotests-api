from clients.errors_schema import ValidationErrorSchema, ValidationErrorResponseSchema
from tools.assertions.base import assert_equals, assert_length


def assert_validation_error(actual: ValidationErrorSchema, expected: ValidationErrorSchema):
    """
    Проверяет, что объект ошибки валидации соответствует ожидаемому значению.

    :param actual: Фактическая ошибка.
    :param expected: Ожидаемая ошибка.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_equals(actual.input, expected.input, 'input')
    assert_equals(actual.type, expected.type, 'type')
    assert_equals(actual.location, expected.location, 'location')
    assert_equals(actual.message, expected.message, 'message')
    assert_equals(actual.context, expected.context, 'context')


def assert_validation_error_response(actual: ValidationErrorResponseSchema,
                                     expected: ValidationErrorResponseSchema):
    """
    Проверяет, что объект ответа API с ошибками валидации (`ValidationErrorResponseSchema`)
    соответствует ожидаемому значению.

    :param actual: Фактический ответ API.
    :param expected: Ожидаемый ответ API.
    :raises AssertionError: Если значения полей не совпадают.
    """
    assert_length(actual.details, expected.details, 'details')

    for index, detail in enumerate(expected.details):
        assert_validation_error(actual.details[index], detail)