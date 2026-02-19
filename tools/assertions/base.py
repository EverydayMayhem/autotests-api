from typing import Any

def assert_status_code(actual: int, expected: int):
    """
    Сравнение статус кодов
    :param actual: фактический статус код
    :param expected: ожидаемый статус код
    :raises AssertionError: если статус коды не совпадают
    """
    assert actual == expected, (
        'Incorrect status code. '
        f'Expected status code: {expected} '
        f'Actual status code: {actual}'
    )

def assert_equals(actual: Any, expected: Any, name: str):
    """
    Проверка значений на равенство
    :param actual: фактическое значение
    :param expected: ожидаемое значение
    :param name: имя поля
    :raises AssertionError: Если фактическое не равно ожидаемому
    """
    assert actual == expected, (
        f'Incorrect value: {name} '
        f'Actual value: {actual} '
        f'Expected value: {expected}'
    )

def assert_is_true(actual: Any, name: str):
    """
    Сравнивает булево (не пустое ли значение
    :param actual:фактическое значение
    :param name:имя
    """
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )