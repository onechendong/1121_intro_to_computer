import socket

HOST = '192.168.137.202'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"connect to {HOST}")

    while True:
        message = input("The Fabonnaci(n) when n = ")
        client_socket.sendall(message.encode())

        if message.lower() == 'exit':
            print("Connection closed.")
            break

        result = client_socket.recv(1024).decode()
        print(f"the ans is {result}")
        break
