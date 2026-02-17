import time

import time
from pydantic import EmailStr, TypeAdapter  # для Pydantic v2 (в v1 было from pydantic.networks import EmailStr)
email_adapter = TypeAdapter(EmailStr)

def get_random_email() -> EmailStr:
    raw_email = f'user.{time.time()}@example.com'
    # Валидируем строку – если она некорректна, будет ошибка
    return email_adapter.validate_python(raw_email)

