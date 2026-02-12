from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, UserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()
create_user_request = UserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

auth_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client = get_files_client(auth_user)
courses_client = get_courses_client(auth_user)

create_file_request = CreateFileRequestDict(
    filename='cat.jpg',
    directory='images',
    upload_file='./testdata/files/cat.jpg'

)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

create_course_request = CreateCourseRequestDict(
    title='Python',
    maxScore=100,
    minScore=10,
    description='Python course',
    estimatedTime='2 weeks',
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)