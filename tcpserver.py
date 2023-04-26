import socket

HOST = ''
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origin = (HOST,PORT)
tcp.bind(origin)
tcp.listen(True)
while True:
	con, client = tcp.accept()
	print "server:Conection Accepted, client:", client
	while True:
		msg = con.recv(2048)
		if not msg:
			break
		print "server:", client," -> ", msg
	print "server:Finishing Conection", client
	con.close()


