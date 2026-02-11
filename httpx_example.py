import httpx

# response_create = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response_create.status_code)
# print(response_create.json())

# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response_create = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
#
# print(response_create.status_code)
# print(response_create.json())
#
# data = {
#     "username": "test",
#     "password": "1234"
# }
# response_create = httpx.post('https://httpbin.org/post', data=data)
#
# print(response_create.status_code)
# print(response_create.json())
#
# headers = {"Authorization": "Bearer mytoken"}
# response_create = httpx.get('https://httpbin.org/get', headers=headers)
#
# print(response_create.request.headers)
# print(response_create.json())
#
# params = {"userId": 1}
# response_create = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
# print(response_create.url)
# print(response_create.json())
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response_create = httpx.post("https://httpbin.org/post", files=files)
#
# print(response_create.json())
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())
# print(response2.json())
#
# client = httpx.Client(headers = headers)
# response_create = client.get('https://httpbin.org/get')
#
# print(response_create.json())

try:
    response = httpx.get('https://jsonplaceholder.typicode.com/invalid')
    response.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка запроса: {e}')

try:
    response = httpx.get('https://httpbin.org/delay/5', timeout = 2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")