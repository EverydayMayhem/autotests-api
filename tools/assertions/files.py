from clients.errors_schema import ValidationErrorResponseSchema, ValidationErrorSchema
from tools.assertions.base import assert_equals

from clients.files.files_model import CreateFileRequestSchema, CreateFileResponseSchema, FileSchema, \
    GetFileResponseSchema
from tools.assertions.errors import assert_validation_error_response


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверка ответа создания файла
    :param request: запрос на создание файла
    :param response: ответ на создание файла
    """
    expected_url = f'http://localhost:8000/static/{request.directory}/{request.filename}'

    assert_equals(expected_url, str(response.file.url), 'url')
    assert_equals(request.filename, response.file.filename, 'filename')
    assert_equals(request.directory, response.file.directory, 'directory')


def assert_file(actual: FileSchema, expected: FileSchema):
    """
    Проверяет, что фактическое значение соответствует ожидаемому
    :param actual:
    :param expected:
    :return:
    """
    assert_equals(actual.id, expected.id, 'id')
    assert_equals(actual.directory, expected.directory, 'directory')
    assert_equals(actual.filename, expected.filename, 'filename')
    assert_equals(actual.url, expected.url, 'url')


def assert_get_file_response(get_file_response: GetFileResponseSchema,
                             create_file_response: CreateFileResponseSchema
                             ):
    """
    Проверяет что ответ на получение файла равен ответу на создание этого файла
    :param get_file_response:
    :param create_file_response:
    :return:
    """
    assert_file(get_file_response.file, create_file_response.file)


def assert_create_file_with_empty_filename_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым именем файла соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустое имя файла.
                ctx={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                msg="String should have at least 1 character",  # Сообщение об ошибке.
                loc=["body", "filename"]  # Ошибка возникает в теле запроса, поле "filename".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_create_file_with_empty_directory_response(actual: ValidationErrorResponseSchema):
    """
    Проверяет, что ответ на создание файла с пустым значением директории соответствует ожидаемой валидационной ошибке.

    :param actual: Ответ от API с ошибкой валидации, который необходимо проверить.
    :raises AssertionError: Если фактический ответ не соответствует ожидаемому.
    """
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="string_too_short",  # Тип ошибки, связанной с слишком короткой строкой.
                input="",  # Пустая директория.
                ctx={"min_length": 1},  # Минимальная длина строки должна быть 1 символ.
                msg="String should have at least 1 character",  # Сообщение об ошибке.
                loc=["body", "directory"]  # Ошибка возникает в теле запроса, поле "directory".
            )
        ]
    )
    assert_validation_error_response(actual, expected)


def assert_get_file_with_incorrect_file_id_response(actual: ValidationErrorResponseSchema):
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type='uuid_parsing',
                input='incorrect-file-id',
                ctx={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
                msg="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                loc=["path", "file_id"]
            )
        ]
    )
    assert_validation_error_response(actual, expected)
