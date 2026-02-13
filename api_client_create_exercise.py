from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, UserRequestDict
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

user_request = UserRequestDict(
    email=get_random_email(),
    password='string',
    lastName='string',
    firstName='string',
    middleName='string',
)
create_user_response = public_user_client.create_user(user_request)
print('Create user data:', create_user_response)

user = AuthenticationUserDict(
    email='user@example.com',
    password='password'
)
files_client = get_files_client(user)
course_client = get_courses_client(user)
exercise_client = get_exercises_client(user)

file_request = CreateFileRequestDict(
    filename='cat.jpg',
    directory='images',
    upload_file='./testdata/files/cat.jpg'
)
create_file_response = files_client.create_file(file_request)
print('Create file data:', create_file_response)

course_request = CreateCourseRequestDict(
    title='AQA Python',
    maxScore=100,
    minScore=60,
    description='Базовый курс автотестирования на Python',
    estimatedTime='3 месяца',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = course_client.create_course(course_request)
print('Create course data:', create_course_response)

exercise_request = CreateExerciseRequestDict(
    title='0.Введение в Python',
    courseId=create_course_response['course']['id'],
    maxScore=100,
    minScore=80,
    orderIndex=0,
    description='Знакомимся с основами Python',
    estimatedTime='2 часа'
)
exercise_response = exercise_client.create_exercise(exercise_request)
print('Create exercise data', exercise_response)