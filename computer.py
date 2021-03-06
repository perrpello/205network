# CST 205 Project 2
# Timothy Dyck and Keith Sylvester
# March 26, 2015

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from Tkinter import *
from subprocess import Popen, PIPE
from array import array
import math
import os

def main():
	# Bash call to run the scanner
	#os.system("scan.sh")
	#fish = `Popen("cat fish | wc -l", shell=True, stdout=PIPE).communicate()[0]`
	#print fish
	#fcount = fish[:-3]
	#fcount = fish[1:]
	#i = int (fcount)
	#print `type(i)`
	#print i
	# Call the ffile function
	cCount = ffile() 

def ffile():
	# Opens the text file for reading
	data = open ("fish.txt", "r")
	# Setting the ip variable to the first subnet
	ip = data.readline()
	ip = ip[19:28]
	#print ip
	# Declaring variables
	sub = []
	compCnt = 1
	tCount = 1
	count = 1
	# Looping through the text file
	for rLine in data.readlines():
		# looping through the text file to pull information 
		stage = rLine[19:28]
		compCnt = compCnt + 1
		if ip == stage:
			#print rLine[19:28]
			count = count + 1
		else:
			sub.append([tCount, ip[6:], count])
			tCount = tCount + 1
			count = 1
			ip = stage
	#print sub
	data.close
	#print compCnt
	# Calling the network function
	network(compCnt, *sub)
	
def network(cont, *num):
	#cir = 360
	canvas_width = 800
	canvas_height = 800
	master = Tk()
	canvas = Canvas(master,	width=canvas_width, height=canvas_height)
	canvas.pack()
	img = PhotoImage(file="jjjj.png")
	imgS = 20
	# pulling the subnet count	
	f = 0
	for (x, y, z) in num:
		if f <= x:
			f = x
	#print f
	#print pltemp
	sl = 2 * math.pi /f
	# Placing the subnets on the canvas
	for i in range (f):
		# setting the angles
		angle = sl * i	
		# Finding the coordinates
		cord1 = int (400 +(300 * (math.sin(angle))))
		cord2 = int (400 + (300 * (math.cos(angle))))
		#print cord1
		#print cord2
		# Printing the images to the canvas
		line = canvas.create_line(390, 390, cord1, cord2)
		canvas.create_image(cord1, cord2, image=img)
		# creating the labels
		for (x, y, z) in num:
			if i+1 == x:
				s=cord2+15
				t=cord1-75
				tName = "10.11." + str(y) + ".x / 24\n" + str(z) + " computers in subnet"
				w = Label(master, text = tName)
				w.pack()
				w.place(x = t, y = s)
		#print pltemp
		#print f
	#while imgS < f * 20:
	#	canvas.create_image(f,20, image=img)
	#	f=f+20
#		f=f+1
	canvas.create_image(390, 390, image=img)
	w = Label(master, text = "router 10.11.0.0 /16 network")
	w.pack()
	w.place(x = 315, y = 405)
	mainloop()

# Calls the main function
main()
