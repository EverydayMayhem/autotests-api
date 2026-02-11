import httpx
from tools.fakers import get_random_email

base_url = 'http://localhost:8000/api/v1'
payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post(f'{base_url}/users', json=payload)
print(response.json())
print(response.status_code)