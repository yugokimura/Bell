#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket
import threading
import thread
import time
import datetime
import os
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import TextToSpeechV1
import pyaudio
import json
import subprocess
import re

TOP_DIR = os.path.dirname(os.path.abspath(__file__))

RESOURCE_FILE = os.path.join(TOP_DIR, "resources/common.res")
DETECT_DING = os.path.join(TOP_DIR, "resources/ding.wav")
DETECT_DONG = os.path.join(TOP_DIR, "resources/dong.wav")
DETECT_ANSW = os.path.join(TOP_DIR, "resources/answer.flac")
DETECT_SORY = os.path.join(TOP_DIR, "resources/sorry.flac")

HOST='127.0.0.1'
PORT=50007
INTERVAL=1

status = { "result" : "" }

class MyThread(threading.Thread):

	def __init__(self):
		super(MyThread, self).__init__()
		self.setDaemon(True)

	def run(self):
		while True:
			result = str(datetime.datetime.today())
			print result
			status["result"] = result
			time.sleep(INTERVAL)

class SubThread(threading.Thread):

	def __init__(self):
		super(SubThread, self).__init__()
		self.setDaemon(True)

	def run(self):
		while True:
			print "MONITORING"
			time.sleep(2)

def handler(conn, addr):
	print addr
	while True:
		data = conn.recv(1024)
		if not data:
			break

		subprocess.call("aplay test1.wav", shell=True)


		print "END PROCESS"

		#print data
		#conn.send(status['result'])
	conn.close()
	print "CLOSE"

def socket_work():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind( (HOST, PORT) )
	s.listen(1)

	while True:
		conn, addr = s.accept()
		thread.start_new_thread(handler, (conn, addr))
	s.close()

if __name__ == '__main__':

	mythread = MyThread()
	mythread.start()

	socket_work()
