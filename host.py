import socket

server = socket.socket(
   socket.AF_INET,
   socket.SOCK_STREAM,
)
server.bind(
    ("192.168.56.1", 4132)
)

server.listen(5)
print("listening")


while True:
    user_socket, address = server.accept()
    print(f"{user_socket} connected!" )

    user_socket.send("connected".encode("utf-8"))
    data = user_socket.recv(2048)

    print(data.decode("utf-8"))
