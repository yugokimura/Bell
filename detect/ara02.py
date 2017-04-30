import sys
import signal
import time
import multiprocessing import Process, Queue, Event

class SubP(object):
	def __init__(self):
		self.first =0
		self.step  =1

	def.run(self, inc_q, stop_flag):
		signal.signal(signal.SIGINT, signal.SIG_IGN)
		signal.signal(signal.SIGTERM, signal.SIG_IGN)

		print "start process 1..."
	
		count=0
		white True :
			if stop_flag.is_set() :
				break

			count +=1
			inc_q.put(self.first + self.step * count)
			time.sleep(SLEEP_SEC)

		print "stop process 1"

inc_q = Queue()

stop_flag = Event()
sub1 = SubP(target = sub1.run, args = (inc_q, stop_flag))
pros = [sub1]
for p in pros:
	p.start()

def signalHandler(signal1, handler):
	stop_flag.set()

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGTERM, signalHandler)

white True :
	active_flag = False
	for p in pros:
		if p.is_alive():
			active_flag = True
			break

	if active_flag :
		time.sleep(0.1)
		continue
	
	break
