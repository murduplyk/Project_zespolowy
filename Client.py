import getpass
import socket

ADDR = ('localhost', 50007)
FORMAT = 'utf-8'
HEADER = 5

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send_msg(msg: str):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    CLIENT.send(send_length)
    CLIENT.send(message)


def send_preordained_msg(msg: str):
    CLIENT.send(msg.encode(FORMAT))


def get_msg() -> str:
    massage_length = int(CLIENT.recv(HEADER).decode(FORMAT))
    return CLIENT.recv(massage_length).decode(FORMAT)


def get_preordained_msg(massage_length: int = 1) -> str:
    return CLIENT.recv(massage_length).decode(FORMAT)


def user_authorization_request() -> list:
    user_not_found = True

    while user_not_found:
        user_name = input('user name: ')
        send_msg(user_name)

        if get_preordained_msg() == 'Y':
            user_not_found = False
        else:
            print('user not found')

    while True:
        user_password = getpass.getpass('password: ')
        send_msg(user_password)

        if get_preordained_msg() == 'Y':
            return [get_preordained_msg(8), get_msg()]


def top_up_balance_request():
    pass


def send_money_request():
    pass


def check_money():
    pass


def withdraw():
    pass
