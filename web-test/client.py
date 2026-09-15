import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

client.send(b"Hello from TCP client!")

data = client.recv(1024)
print("Server replied:", data.decode())

client.close()