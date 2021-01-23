import socket


client = socket.socket(
   socket.AF_INET,
   socket.SOCK_STREAM,
)

client.connect (
     ("192.168.56.1", 4132)
 )

while True:
     data = client.recv(2048)
     print(data.decode("utf-8"))

     client.send(input(":::").encode("utf-8"))
