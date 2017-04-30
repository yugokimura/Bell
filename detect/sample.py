import sys
import signal
import os

cmd = "/usr/bin/sox -c 1 -S -d test.wav silence 1 0.3 2.5% 1 0.3 4.7%"
os.system(cmd)
