import socket 

#this code is for sending and receive udp


UDP_IP = "192.168.1.177"
UDP_PORT = 8888
message = "rams r3"
localPort = 3241

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # this means we are using UDPcntrl questions mark for comment
sock.bind(("", localPort)) #automatic ip, localPort

for x in range(1,100):
    sock.sendto(bytes(message, "utf-8"), (UDP_IP, UDP_PORT)) #sending 
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes #receiving from the UDP_IP 
    print("received message: %s" % data) #printing the received in the terminal


