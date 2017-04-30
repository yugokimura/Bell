import snowboydecoder
import sys
import signal
import time
import os

f = open('sig.pid', 'r')
str =f.read()
f.close()

os.kill(int(str), signal.SIGINT)
