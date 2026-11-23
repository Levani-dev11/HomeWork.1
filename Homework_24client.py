import socket

HOST = "127.0.0.1"
PORT = 5060
MESSAGE = "hello socket"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(MESSAGE.encode("utf-8"))
    response = client.recv(1024)
    print(f"პასუხი: {response.decode('utf-8')}")