import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 547))

name = input('Enter your name: ')
s.send(bytes(name, 'utf-8'))

msg = s.recv(1024)
d = pickle.loads(msg)
print(d)



