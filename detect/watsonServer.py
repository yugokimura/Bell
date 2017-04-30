import socket
import threading
import time
import datetime

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

def Stt(fname):
	STT = SpeechToTextV1( username = "4b01ef0b-1d88-4d81-8702-9e4d0c220322",
        	password =  "BLbpaO6ImMP2",
                x_watson_learning_opt_out=False)
	
	with open(fname, 'rb') as audio_file:
		res = STT.recognize(
			audio_file,
                	model='ja-JP_NarrowbandModel',
                	content_type='audio/wav',
                	timestamps=True,
                	word_confidence=True
		)
	data = json.loads(res)
	
def Tts(fname, text):
	TTS = TextToSpeechV1( username = "1ed123c6-5c8e-4fa7-a4f1-9462320767f3",
		password =  "1cHpBkgkbXfv",
		x_watson_learning_opt_out=False)

	with open(fname, 'wb') as audio_file:
		audio_file.write(TTS.synthesize(text, accept='audio/wav', voice="ja-JP_EmiVoice"))

	subprocess.call("aplay " + fname, shell=True)


class SttThread(threading.Thread):
	
	def __init__(self):
		super(SttThread, self).__init__()
		self.setDaemon(True)

	def setText(self, txt):
		self.txt = txt

	def run(self):
		print self.txt

def socket_work():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind( (HOST, PORT) )
	s.listen(1)

	while True:
		conn, addr = s.accept()
		print 'Connected by', addr
		data = conn.recv(1024)
		print data
		conn.send(status['result'])
		conn.close()

	s.close()

if __name__ == '__main__':

	mythread = MyThread()
	mythread.start()

	m2 = SttThread()
	m2.setText('hello')
	m2.start()

	socket_work()
