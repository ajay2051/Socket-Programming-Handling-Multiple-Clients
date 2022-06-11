import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 564))

def send(message):
    s.send(bytes(message,'utf-8'))
send('Ajay')
send('Bijay')

# name = input('Enter your name: ')
# s.send(bytes(name, 'utf-8'))

msg = s.recv(1024).decode('utf-8')
print(msg)


