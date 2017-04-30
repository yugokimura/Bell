import snowboydecoder
import sys
import signal
import commands
import os

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    print "signal_handler"
    interrupted = True


def interrupt_callback():
    global interrupted
    #print "interrupt_callback"
    return interrupted


def alexa_cb():
	global interrupted
	print "alexa WAS CALLED UPPPPPPPPPPPPPPPPPPP ALEXA"

def cortana_cb():
	global interrupted
	print "cortana WAS CALEED UPPPPPPPPPPPPPPPPPPPPPPP CORTANA"	

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1:]
callback = [lambda: alexa_cb, lambda: cortana_cb]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')


detector.start(detected_callback=callback,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
