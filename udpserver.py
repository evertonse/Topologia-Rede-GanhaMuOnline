
import socket
HOST = ''
PORT = 5000
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
origin = (HOST,PORT)
udp.bind(origin)
while True:
	msg, client = udp.recvfrom(2048)
	print "this is what we got from the udp.recv from :"
	print client, msg
udp.close()

