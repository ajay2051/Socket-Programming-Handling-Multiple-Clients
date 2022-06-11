import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 547))
s.listen(5)

while True:

    clientsocket, address = s.accept()

    print(f"Connection with {address} has been established.")

    name = clientsocket.recv(1024).decode('utf-8')
    print(name)
    
    clientsocket.send(bytes("Hey there!!!","utf-8"))


    
    


# import asyncio

# async  def main():
#     print('Hello .....')
#     await asyncio.sleep(1)
#     print('....World')
# asyncio.run(main()) 

    