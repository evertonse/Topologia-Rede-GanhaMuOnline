import socket
HOST = '127.0.0.1'
PORT = 5000
dest = (HOST,PORT)
tcp = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)

tcp.connect(dest)
print '"crtl + c" or "crtl + x" to quit'
msg = raw_input()
while msg <> '\x18':
	tcp.send(msg)
	msg = raw_input()
tcp.close()
