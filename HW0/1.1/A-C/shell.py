#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from datetime import date
import subprocess

#pipeline parameter for number of folder
N = int(sys.argv[1])

#output of local process directory
def getlist():
	stream = subprocess.run(['ls','-l'], stdout = subprocess.PIPE)
	out = stream.stdout.decode('utf-8')
	return out

#current directory
direc = os.getcwd()

#loop for individual folders
for i in range(N):
	#new folder path and
	path = direc + '/New' + str(i)
	#subdirectories and solution/data.txt files
	path1 = path + '/output'
	path2 = path + '/input'
	os.makedirs(path1)
	os.chdir(path1)
	os.mknod('solution.txt')
	os.makedirs(path2)
	os.chdir(path2)
	os.mknod('data.txt')
	#log.txt
	os.chdir(path)
	f = open('log.txt','a')
	f.write(str(date.today()) + '\n')
	f.write(getlist())
	f.close()
