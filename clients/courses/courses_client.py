from clients.api_client import APIClient
from httpx import Response, URL
from typing import TypedDict

from clients.private_http_builder import get_private_http_client, AuthenticationUserDict


class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов.
    """
    userId: str


class CreateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class UpdateCourseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None


class CoursesClient(APIClient):
    """
    Класс для работы с /courses
    """

    def get_all_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/courses', params=query)

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/courses', json=request)

    def update_course_api(self, request: UpdateCourseRequestDict) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch('/api/v1/courses', json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/courses/{course_id}')


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
