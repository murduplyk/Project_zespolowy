import threading
import socket
import random
import json


ADDR = ('localhost', 50007)
FORMAT = 'utf-8'
HEADER = 5
ACCOUNTS_DATA = r'Server\Accounts.json'


SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((ADDR))

def get_msg(conn) -> str:
    massage_length = int(conn.recv(HEADER).decode(FORMAT))
    return conn.recv(massage_length).decode(FORMAT)

def send_msg(conn,msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    conn.send(send_length)
    conn.send(message)

def send_preordained_msg(conn, msg: str):
    conn.send(msg.encode(FORMAT))

def get_preordained_msg(conn,massage_length: int) -> str:
    return conn.recv(massage_length).decode(FORMAT)

def handle_client(conn, addr):
    account_number = None
    connected = True

    while connected:
        pass



def start():
    SERVER.listen(0)
    while True:
        conn, addr = SERVER.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f'{addr} is connected\nCount of active conection {threading.active_count() - 1}\n')


if __name__ == '__main__':
    print(f'server is starting...')
    start()