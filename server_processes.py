from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from fib import fib
from threading import Thread
from concurrent.futures import ProcessPoolExecutor

pool = ProcessPoolExecutor()


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connecting", addr)
        Thread(target=fib_handler, args=(client,), daemon=True).start()


def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        future = pool.submit(fib, n)
        result = future.result()
        resp = str(result).encode("ascii") + b"\n"
        client.send(resp)


if __name__ == "__main__":
    fib_server(("", 25000))
