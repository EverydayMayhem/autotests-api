from clients.api_client import APIClient
from httpx import Response

from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_model import GetExerciseQuerySchema, GetExercisesResponseSchema, \
    CreateExerciseRequestSchema, UpdateExerciseRequestSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema


class ExercisesClient(APIClient):
    """
    Класс для работы с /exercise
    """

    def get_exercises_api(self, query: GetExerciseQuerySchema) -> Response:
        """
        Метод для получения заданий по айди курса

        :param query: параметры запроса, courseId - айди курса по которому получаем список занятий
        :return: возвращает объект типа httpx.Response
        """
        return self.get('/api/v1/exercises', params=query.model_dump(by_alias=True))

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод для создания заданий

        :param request: тело запроса с обязательными полями title, courseId,
        maxScore, minScore, orderIndex, description, estimatedTime
        :return: возвращает объект типа httpx.Response
        """
        return self.post('/api/v1/exercises', json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод для частичного обновления задания

        :param exercise_id: идентификатор занятия
        :param request: тело запроса с обязательными полями title,
        maxScore, minScore, orderIndex, description, estimatedTime
        :return: возвращает объект типа httpx.Response
        """
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request.model_dump(by_alias=True))

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

    def get_exercises(self, query: GetExerciseQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод-обертка над get_exercises_api для получения json - получение всех занятий
        :param query: GetExerciseQueryDict
        :return: объект GetExercisesResponse
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод-обертка для получения json занятия по ид
        :param exercise_id: идентификатор занятия
        :return: объект GetExerciseResponse
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> GetExercisesResponseSchema:
        """
        Метод-обертка для получения json обновленного занятия по ид
        :param exercise_id: идентификатор занятия
        :param request: объект UpdateExerciseRequestDict
        :return: объект GetExerciseResponse
        """
        response = self.update_exercise_api(exercise_id, request)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод-обертка для получения json создания занятия
        :param request: объект CreateExerciseRequestDict
        :return: объект GetExerciseResponse
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user))
