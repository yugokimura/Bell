import socket
import os
import threading

class DataLink():

	host = '127.0.0.1'
	port = 5008
	def __init__(self, param = (host, port)):
		if param[0]:
			self.host = param[0]

	def start(self, param):
		print param
		

d =  DataLink( ('127.0.0.1', 50007) )

HOST='127.0.0.1'
PORT=50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s.getsockname()

try:
	s.connect( (HOST, PORT) )
	s.send('OK')
	s.send('long time time')
	s.send('this this hiss shisis')
	s.send('SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
	data = s.recv(1024)
	print 'Received', repr(data)
except Exception as e:
	print("error: %s" % (e))
finally:
	s.close()
