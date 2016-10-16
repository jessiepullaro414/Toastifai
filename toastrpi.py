# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import serial
from twilio.rest import TwilioRestClient 
ser = serial.Serial('/dev/ttyACM4',9600)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

while True :
	val = int(ser.readline())
	print(val)
	if val == 1 :
		# put your own credentials here
		client = TwilioRestClient(account='AC24b3c0ad866586038e4f5ca818ae30ed',token='3bab3d6d5bef27855cfb5bada3c39346')
		client.messages.create(to="+14077583284",from_="+14079019282", body="TOAST")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(2,GPIO.OUT)
		GPIO.output(2,GPIO.LOW) 

		time.sleep(1)
		GPIO.output(2,GPIO.HIGH)
		GPIO.cleanup()

