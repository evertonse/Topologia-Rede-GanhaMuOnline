from socket import socket, AF_INET,SOCK_DGRAM
HOST = '127.0.0.1' # Server's IP
PORT = 5000
udp = socket(AF_INET, SOCK_DGRAM)
dest = (HOST,PORT)
print "Crtl + X to leave"
msg = raw_input()
while msg <> '\x18':
	udp.sendto(msg,dest)
	msg = raw_input()
udp.close()
