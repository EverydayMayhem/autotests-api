from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from clients.files.files_model import FileSchema
from clients.users.users_model import UserSchema

class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    user_id: str

class CourseSchema(BaseModel):
    """
    Описание структуры курса
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    id: str
    title: str
    max_score: int = Field(default=0)
    min_score: int = Field(default=0)
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema

class GetCourseResponseSchema(BaseModel):
    """
    Описание ответа создания курса
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    course: CourseSchema

class CreateCourseResponseSchema(BaseModel):
    """
    Описание ответа создания курса
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    course: CourseSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str
    max_score: int = Field(default=0)
    min_score: int = Field(default=0)
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str | None
    max_score: int | None = Field(default=0)
    min_score: int | None = Field(default=0)
    description: str | None
    estimated_time: str | None