import socket
import time

#growing pot 1 192.168.0.1
#growing pot 2 192.168.0.2
#growing pot 3 192.168.0.3
#server 192.168.0.0(255)


def UDP_RequestInfoFromGrowPod(ipAddress):
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    encoding = 'utf-8'
    send_data="req"
    client_socket.sendto(send_data.encode(encoding),ipAddress)
    try:
        init_data,addr=client_socket.recvfrom(4096)
        rec_data=init_data.decode(encoding) 
        return rec_data
    except:
        pass
def UDP_TransferUpdateToGrowPod(ipAddress,updatePacket):
    client_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    encoding = 'utf-8'
    send_data=updatePacket
    client_socket.sendto(send_data.encode(encoding),ipAddress)


