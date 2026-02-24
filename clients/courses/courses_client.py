from clients.api_client import APIClient
from httpx import Response, URL

from clients.courses.courses_model import GetCoursesQuerySchema, CreateCourseRequestSchema, \
    UpdateCourseRequestSchema, CreateCourseResponseSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema


class CoursesClient(APIClient):
    """
    Класс для работы с /courses
    """

    def get_all_courses_api(self, query: GetCoursesQuerySchema) -> Response:
        """
        Метод получения списка курсов.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get('/api/v1/courses', params=query.model_dump(by_alias=True))

    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f'/api/v1/courses/{course_id}')

    def create_course_api(self, request: CreateCourseRequestSchema) -> Response:
        """
        Метод создания курса.

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime,
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post('/api/v1/courses', json=request.model_dump(by_alias=True))

    def update_course_api(self, course_id: str, request: UpdateCourseRequestSchema) -> Response:
        """
        Метод обновления курса.

        :param course_id: Идентификатор курса.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f'/api/v1/courses/{course_id}', json=request.model_dump(by_alias=True))

    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f'/api/v1/courses/{course_id}')

    def create_course(self, request: CreateCourseRequestSchema) -> CreateCourseResponseSchema:
        """
        Обертка над create_course_api для возвращения json
        :param request: CreateCourseRequestDict
        :return: GetCourseResponse
        """
        response = self.create_course_api(request)
        return CreateCourseResponseSchema.model_validate_json(response.text)


def get_courses_client(user: AuthenticationUserSchema) -> CoursesClient:
    """
    Метод создает http-client с авторизационными заголовками
    :param user: объект типа AuthenticationUserDict с обязательными email и password
    :return: объект класса CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user))
