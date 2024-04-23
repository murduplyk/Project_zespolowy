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


def find_user(find_by: str,
              find):
    with open(ACCOUNTS_DATA) as f:
        data = json.load(f)
    user = [user for user in data["Users"] if user[find_by] == find]
    if user:
        return user[0]
    else:
        return None


def create_user(conn,
                addr):
    # username
    while True:
        user_name = get_msg(conn)
        print(f'[{addr[0]}]user name: {user_name}')

        if not find_user('user name', user_name):
            send_preordained_msg(conn, 'Y')
            break
        else:
            send_preordained_msg(conn, 'N')
    # password
    user_pass = get_msg(conn)
    # create account number
    while True:
        account_number = random.randint(10000000, 99999999)
        if not find_user('account number', account_number):
            print(f'[{addr[0]}] account number: {account_number}')
            break

    # create user
    user = {
        "user name": f"{user_name}",
        "password": f"{user_pass}",
        "account number": f"{account_number}",
        "amount of money": 0
    }
    # save user
    with open(ACCOUNTS_DATA) as f:
        data = json.load(f)
    data['Users'].append(user)
    with open(ACCOUNTS_DATA, 'w') as f:
        json.dump(data, f, indent=2)


def delete_user(conn):
    while True:
        account_number = get_msg(conn)
        user = find_user("account number", account_number)
        if user:
            send_preordained_msg(conn, 'Y')
        else:
            send_preordained_msg(conn, 'N')
            continue

        if get_preordained_msg(conn, 1):
            break

        with open('Server/Accounts.json') as f:
            data = json.load(f)
        try:
            user_index = data['Users'].index(user)
            del data['Users'][user_index]

            with open('Server/Accounts.json', 'w') as f:
                json.dump(data, f, indent=2)
        except ValueError:
            send_msg(conn, 'User not found or has already been deleted')
            break
        send_msg(conn, 'User deleted')


def change_user_data(conn):
    while True:
        find_by = get_msg(conn)
        find = get_msg(conn)

        if find_user(find_by, find):
            send_preordained_msg(conn, 'Y')
            break
        else:
            send_preordained_msg(conn, 'N')

    change_by = get_msg(conn)
    change = get_msg(conn)

    with open(ACCOUNTS_DATA) as f:
        data = json.load(f)
    for user in data['Users']:
        if user[find_by] == find:
            user[change_by] = change if change_by == 'password' \
                else int(change)
            break
    with open(ACCOUNTS_DATA, 'w') as f:
        json.dump(data, f, indent=2)


def authorization_user(conn):
    user_not_found = True
    user_data = {}
    while user_not_found:
        user_name = get_msg(conn)
        user_data = find_user('user name', user_name)

        if user_data:
            send_preordained_msg(conn, 'Y')
            user_not_found = False
        else:
            send_preordained_msg(conn, 'N')

    incorrect_password = True

    while incorrect_password:
        user_password = get_msg(conn)

        if user_data['password'] == user_password:
            incorrect_password = False
            send_preordained_msg(conn, 'Y')
            send_preordained_msg(conn, user_data['account number'])
            send_msg(conn, str(user_data['amount of money']))
            return user_data['account number']
        else:
            send_preordained_msg(conn, 'n')

def get_money():
    pass



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