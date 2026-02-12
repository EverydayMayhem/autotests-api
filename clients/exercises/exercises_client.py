from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExerciseQueryDict(TypedDict):
    """
    Структура query-параметров для получения всех занятий по курсу
    """
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """
    Структура тела запроса для создания занятий
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
    Структура тела запроса для обновления занятия
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Класс для работы с /exercise
    """

    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод для получения заданий по айди курса

        :param query: параметры запроса, courseId - айди курса по которому получаем список занятий
        :return: возвращает объект типа httpx.Response
        """
        return self.get('/api/v1/exercises', params=query)

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания заданий

        :param request: тело запроса с обязательными полями title, courseId,
        maxScore, minScore, orderIndex, description, estimatedTime
        :return: возвращает объект типа httpx.Response
        """
        return self.post('/api/v1/exercises', json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод для частичного обновления задания

        :param exercise_id: идентификатор занятия
        :param request: тело запроса с обязательными полями title,
        maxScore, minScore, orderIndex, description, estimatedTime
        :return: возвращает объект типа httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания по id

        :param exercise_id: идентификатор занятия
        :return: возвращает объект типа httpx.Response
        """
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по id

        :param exercise_id: идентификатор занятия
        :return: возвращает объект типа httpx.Response
        """
        return self.delete(f'/api/v1/exercises/{exercise_id}')


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
