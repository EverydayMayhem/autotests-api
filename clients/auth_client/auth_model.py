from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию
    """
    email: EmailStr
    password: str


class TokenSchema(BaseModel):  # Добавили структуру с токенами аутентификации
    """
    Описание структуры аутентификационных токенов.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    token_type: str
    access_token: str
    refresh_token: str


class LoginResponseSchema(BaseModel):  # Добавили структуру ответа аутентификации
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str  # Название ключа совпадает с API