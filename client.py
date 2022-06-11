import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 547))

name = input('Enter your name: ')
s.send(bytes(name, 'utf-8'))

msg = s.recv(1024)
print(msg.decode("utf-8"))



