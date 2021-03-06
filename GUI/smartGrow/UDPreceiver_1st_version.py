import socket
import time

def UDP_RequestInfoFromGrowPod(ipAddress):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(10)
    encoding = 'utf-8'
    send_data = "req 0 0 0 0"
    client_socket.sendto(send_data.encode(encoding),(ipAddress, 80))
    try:
        init_data, addr = client_socket.recvfrom(4096)
        rec_data = init_data.decode(encoding)
        return rec_data
    except:
        print("UDP Fail.")
        return "fail"

def UDP_TransferUpdateToGrowPod(ipAddress,updatePacket):
    print(updatePacket)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1)
    encoding = 'utf-8'
    send_data = updatePacket
    # print(send_data)
    client_socket.sendto(send_data.encode(encoding), (ipAddress, 80))
