from typing import Any, Sized
import allure
from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Assert that status code equals {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Сравнение статус кодов
    :param actual: фактический статус код
    :param expected: ожидаемый статус код
    :raises AssertionError: если статус коды не совпадают
    """
    logger.info(f'Assert that status code equals {expected}')
    assert actual == expected, (
        'Incorrect status code. '
        f'Expected status code: {expected} '
        f'Actual status code: {actual}'
    )


@allure.step("Assert that {name} equals {expected}")
def assert_equals(actual: Any, expected: Any, name: str):
    """
    Проверка значений на равенство
    :param actual: фактическое значение
    :param expected: ожидаемое значение
    :param name: имя поля
    :raises AssertionError: Если фактическое не равно ожидаемому
    """
    logger.info(f'Assert that "{name}" equals {expected}')
    assert actual == expected, (
        f'Incorrect value: {name} '
        f'Actual value: {actual} '
        f'Expected value: {expected}'
    )


@allure.step("Assert that {name} is True")
def assert_is_true(actual: Any, name: str):
    """
    Сравнивает булево (не пустое ли значение
    :param actual:фактическое значение
    :param name:имя
    """
    logger.info(f'Assert that "{name}" is True')
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    """
        Проверяет, что длины двух объектов совпадают.

        :param name: Название проверяемого объекта.
        :param actual: Фактический объект.
        :param expected: Ожидаемый объект.
        :raises AssertionError: Если длины не совпадают.
    """
    with allure.step(f"Assert that {name} is {len(expected)} length"):
        logger.info(f'"Assert that "{name}" is {len(expected)} length')

        assert len(actual) == len(expected), (
            f'Length mismatch for object: {name} '
            f'Expected length: {len(expected)} '
            f'Actual length: {len(actual)}'
        )
