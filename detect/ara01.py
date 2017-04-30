import snowboydecoder
import sys
import signal
import time
import os

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
pid = os.getpid()
f = open('sig.pid', 'w')
f.write(str(pid))
f.close()

while True:
	if interrupted == True:
		break

	time.sleep(1)


os.remove('sig.pid')
print "process break"
