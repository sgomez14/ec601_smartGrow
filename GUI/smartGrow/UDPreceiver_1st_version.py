import socket
import time
#growing pot 1 192.168.0.1
#growing pot 2 192.168.0.2
#growing pot 3 192.168.0.3
#server 192.168.0.0(255)
def UPD_client():
    address=('10.0.0.1', 8888)
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    encoding = 'utf-8'

    while(1):
        send_data="lux"
        client_socket.sendto(send_data.encode(encoding),address)
        try:
            init_data,addr=client_socket.recvfrom(4096)
            rec_data=int.from_bytes(init_data,byteorder='big')
        except:
            print("wrong connect")


