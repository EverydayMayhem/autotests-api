import httpx
from tools.fakers import get_random_email

base_url = 'http://localhost:8000/api/v1'
payload_create = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response_create = httpx.post(f'{base_url}/users', json=payload_create)
response_create_body = response_create.json()
print(response_create_body)
print(response_create.status_code)

payload_login = {
  "email": payload_create['email'],
  "password": payload_create['password']
}

response_login = httpx.post(f'{base_url}/authentication/login', json=payload_login)
response_login_body = response_login.json()
print(f'Login data: {response_login_body}')
print(f'Status code = {response_login.status_code}')

user_id = response_create_body['user']['id']
headers = {'Authorization':f'Bearer {response_login_body['token']['accessToken']}'}
response_get_userid = httpx.get(f'{base_url}/users/{user_id}', headers=headers)
response_get_userid_body = response_get_userid.json()
print(f'Данные юзера {user_id}: {response_get_userid_body}')
print(f'Статус код: {response_get_userid.status_code}')