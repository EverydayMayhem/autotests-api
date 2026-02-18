from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from tools.fakers import fake

class ExerciseSchema(BaseModel):
    """
    Описание структуры Занятий
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    id: str
    title: str
    course_id: str
    max_score: int = Field(default=0)
    min_score: int = Field(default=0)
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение всех занятий
    """
    exercise: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры на получение занятия по ид
    """
    exercise: ExerciseSchema

class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры на получение занятия по ид
    """
    exercise: ExerciseSchema

class GetExerciseQuerySchema(BaseModel):
    """
    Структура query-параметров для получения всех занятий по курсу
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    course_id: str


class CreateExerciseRequestSchema(BaseModel):
    """
    Структура тела запроса для создания занятий
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str = Field(default_factory=fake.sentence)
    course_id: str
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Структура тела запроса для обновления занятия
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)