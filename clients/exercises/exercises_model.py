from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

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

    title: str
    course_id: str
    max_score: int = Field(default=0)
    min_score: int = Field(default=0)
    order_index: int
    description: str
    estimated_time: str


class UpdateExerciseRequestSchema(BaseModel):
    """
    Структура тела запроса для обновления занятия
    """
    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)

    title: str | None
    max_score: int | None = Field(default=0)
    min_score: int | None = Field(default=0)
    order_index: int | None
    description: str | None
    estimated_time: str | None