import socket

HOST = "127.0.0.1"
PORT = 5060

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print("სერვერი ელოდება კლიენტს...")

    connection, address = server.accept()
    with connection:
        data = connection.recv(1024)
        text = data.decode("utf-8")
        print(f"მივიღეთ: {text}")
        connection.sendall(text.upper().encode("utf-8"))

print("სერვერი დასრულდა")
