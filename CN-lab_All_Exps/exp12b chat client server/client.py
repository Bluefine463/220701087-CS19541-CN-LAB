import socket

def recvr2(a):
    host='127.0.0.1'
    port=12345
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.sendto(a.encode(),(host,port))
        data,addr=s.recvfrom(1024)
        print({data.decode()})
while(True):
    a=input("Enter Message ")
    if (a=="end"):
        recvr2(a)
        break
    else:
        recvr2(a)