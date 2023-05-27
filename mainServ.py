from Server import Server
import threading
from modules.Commands import Commands
# TODO:
#    Обработка ввода команд и общения сервер<->клиент

s = Server()

# def wait():
while True:
    c, addr = s.sock.accept()
    client = threading.Thread(target=s.wait_client, args=[c, addr])
    client.start()
    print(threading.active_count())

# wait_clients = threading.Thread(target=wait)
# wait_clients.start()

# TODO: Поключить команды из класса Commands
# cmds = Commands('/')
#
# while cmd != 'exit':
#     cmd = input('Введите команду: ').split()
#
#     args = tuple(cmd[1:])
#     cmd = cmd[0]
#
#     cmd = cmds._call(cmd)
#     if cmd is False:
#         print('Команды не существует')
#         continue
#
#     # print(cmd(*args))
#     cmd(*args)
#
#     if cmd == 'exit':
#         exit()
#     if cmd=='pause':
#         pass
#     if cmd=='logs':
#         pass
#     if cmd=='del logs':
#         pass
#     if cmd=='del auth':
#         pass
