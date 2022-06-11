import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((socket.gethostname(), 564))
    print(socket.gethostname())
except socket.error as e:
    print(str(e))
    





def handle_client(client, address):
    print(f'Connection with {address} has been established')
    while True:

        msg = client.recv(1024).decode('utf-8')
        print(msg)

        client.send(bytes('Hello','utf-8'))
    # client.close()
        
        
def start():
    s.listen()
    while True:
        client,address  = s.accept()
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()
        thread.join()
        print(f'Active Connections: {threading.activeCount() - 1}') # -1 because one thread is always started

start()

