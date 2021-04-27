#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, out)
GPIO.setup(24, out)
GPIO.setup(26, out)

red = 10
blue =10
rup =1
bup = 1
r=GPIO.PWM(22, 50)
g=GPIO.PWM(24, 50)
b=GPIO.PWM(26, 50)
while true:
	r.start(freq)
	g.start(freq)
	b.start(freq)
	if red < 100 and rup :
		red= red + 5
		if red >= 100 :
			rup = 0
		r.ChangeDutyCycle(red)
		g.ChangeDutyCycle(red)
		b.ChangeDutyCycle(red)
		time.sleep(1)
	elif not rup :
		red = red -5
		if red <= 10:
			rup =1
		r.ChangeDutyCycle(red)
		g.ChangeDutyCycle(red)
		b.ChangeDutyCycle(red)
		time.sleep(1)
		
	if red < 100 and up :
		blue= blue + 5
		if blue >= 100 :
			bup = 0
		r.ChangeDutyCycle(blue)
		g.ChangeDutyCycle(blue)
		b.ChangeDutyCycle(blue)
		time.sleep(1)
	elif not bup :
		red = blue -5
		if blue <= 10:
			bup =1
		r.ChangeDutyCycle(blue)
		g.ChangeDutyCycle(blue)
		b.ChangeDutyCycle(blue)
		time.sleep(1)
		
		
		
		
