import socket

HOST = '127.0.0.1'
PORT = 22222

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Ping')
    data = s.recv(1024)

print('{} recebido'.format(repr(data)))