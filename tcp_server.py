import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_adress = ('localhost', 12345)
    server_socket.bind(server_adress)

    server_socket.listen(5)
    print("Сервер запущен и ждет подключений...")

    while True:
        client_socket, client_adress = server_socket.accept()
        print(f'Подключение от {client_adress}')

        data = client_socket.recv(1024).decode()
        print(f'Получено сообщение: {data}')

        response = f'Сервер получил сообщение: {data}'
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == '__main__':
    server()