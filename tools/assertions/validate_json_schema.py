from typing import Any
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Валидация через jsonschema
    :param instance: что сравниваем
    :param schema: с чем сравниваем
    :return:
    """
    validate(
        schema=schema,
        instance=instance,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )