import httpx
from tools.fakers import fake

base_url = 'http://localhost:8000/api/v1'
payload_create = {
  "email": fake.email(),
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
print(f'Статус код: {response_login.status_code}')

create_file_headers = {
    "Authorization": f"Bearer {response_login_body['token']['accessToken']}"
}
create_file_response = httpx.post(
    f'{base_url}/files',
    data={"filename": "cat.jpg", "directory": "images"},
    files={"upload_file": open('./testdata/files/cat.jpg', 'rb')},
    headers=create_file_headers
                                  )
create_file_response_data = create_file_response.json()
print('Create file data: ', create_file_response_data)