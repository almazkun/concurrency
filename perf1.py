from time import time
from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(("localhost", 25000))


while True:
    start = time()
    sock.send(b"30")
    resp = sock.recv(100)
    print(time() - start)
