from pydantic import BaseModel, Field, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель для описания User
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

class CreateUserRequestSchema(BaseModel):
    """
    Модель для описания запроса на создание пользователя
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True, )

    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str

class CreateUserResponseSchema(BaseModel):
    user: UserSchema