import socket

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

HOST = '192.168.137.202'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    while True:
        print("Waiting for connection...")
        conn, addr = server_socket.accept()
        print(f"Add connection from {addr}")

        #with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Closed connection.")
                break

            client_ip, client_port = addr
            print(f"Received from ('{client_ip}', {client_port}): {data.decode()}")

            try:
                n = int(data.decode())
                result = fibonacci(n)
                conn.sendall(str(result).encode())
                print(f"Send to ('{client_ip}', {client_port}): {result}")
            except :
                pass
                
            print("connection closed")
            break
        
             
