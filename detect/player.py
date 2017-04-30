#!/usr/python

import subprocess
a = "resources/answer.flac"
subprocess.call("aplay resources/answer.flac", shell=True)
