import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("127.0.0.1",5000))
server.listen(1)

print("Tcp server is waiting")

conn, addr = server.accept()
print("connected by address:",addr)

data = conn.recv(1024)
print("Received:",data.decode())

conn.send(b"Hello from tcp server!")

conn.close()
server.close()