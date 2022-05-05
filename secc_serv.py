####################
#Author: Daniel Jones
#Language: Python 3.10.2
#IDE: Atom
#OS: Windows/PopOS
####################
import threading
import socket



clients = []
nicknames = []

#todo: Will need to set up way to get public-facing IP automatically to save to conf file.
#Using localhost for testing.


host = '127.0.0.1'
#9 for men 7 for dwarves, 3 for elves, and 1 secret
port = 9731

print("host is ", host, " port is ", port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#broadcasts message to every client.
def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            #if exception, removes IP and nickname from list.
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        #prompts client to ask for nickname and adds to list.
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(f'Nickname is {nickname}!')
        broadcast(f'{nickname} has joined the chat.')

        client.send("connected to the server.".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client))
        thread.start()

receive()
#reads configuration file.
#config file contains IP address and preferred port. Default port is 9731, but is changeable if user wants something else.
def getConf():
    try:
        confFile = open("server.conf", "rt")

    except:
        print("server.conf not found. Creating...")
