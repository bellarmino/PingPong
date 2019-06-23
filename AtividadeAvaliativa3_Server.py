import socket
import time
from multiprocessing import Process, Queue
import threading

HOST = '127.0.0.1'
PORT = 22222


def ping(conn, addr):
    with conn:
        # time.sleep(10)
        print('Conectado a', addr)
        while True:
            data = conn.recv(1024)
            if not data == b'Ping':
                break
            print('{} recebido de {}'.format(data, addr))
            conn.sendall(b'Pong')


def connection():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Aguardando')
        conn, addr = s.accept()
        print('Conexão aceita')

        t = threading.Thread(target=ping, args=(conn,addr))
        t.start()


while True:
    connection()