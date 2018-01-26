#!/usr/bin/env python3

import os

print("\n********* Running a Python program as a Shell Script ********")
print("Using os.system to execute 'pwd'")
os.system('pwd')
print("That was not all that impressive.")
print("Let's try ls -a")
os.system('ls -a')
print("Equally unimpressive.")
print("How about reboot? Just kidding.")
print("********* Ending a Python program as a Shell Script ********\n")

