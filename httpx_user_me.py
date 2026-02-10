import httpx

base_url = 'http://localhost:8000/api/v1'
login_payload = {
  "email": "user@example.com",
  "password": "password"
}
login_response = httpx.post(f'{base_url}/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Данные ответа на запрос login: {login_response_data}')
print(f'Статус код ответа: {login_response.status_code}')

headers = {"Authorization": f'Bearer {login_response_data['token']['accessToken']}'}
user_me_response = httpx.get(f'{base_url}/users/me', headers=headers)
user_me_response_data = user_me_response.json()
print(f'Данные ответа на запрос users/me: {user_me_response_data}')
print(f'Статус код ответа: {user_me_response.status_code}')