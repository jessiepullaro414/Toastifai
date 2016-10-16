#this is a project made at hackriddle 2016
#it is a "smart" toaster using clarifai, simplecv, and twilio
#by: Jessie Pullaro, Frank Calas, Max Farrel and Kyle Spomer
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import serial
from twilio.rest import TwilioRestClient
from clarifai import rest
from clarifai.rest import ClarifaiApp
import cv2
from PIL import Image, ImageEnhance
ser = serial.Serial('/dev/ttyACM4',9600)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)


#while True :        
#	val = int(ser.readline())
#        print(val)
#        if val == 1 :
#		break

file = "current_image.png"


camera_port = 0
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
app = ClarifaiApp("UHgwtsynZgd19kC1f46FoNulBsdglENG5oF9Dwwc", "VBP5o33oTh6Whpt7nZyg-gAa1GV9ZoKDZktJ4vBe")#pulls the api keys from keys.py

model = app.models.get("toast")

toast_perfect = 0.3
toast_done = False
toast_counter = 0
# predict with samples

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im


while (toast_done != True or toast_counter == 3):
    camera_capture = get_image()

    cv2.imwrite(file, camera_capture)
    #PIL stuff
    img = Image.open(file)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(2.0)
    img2.save(file)


    model_json = model.predict_by_filename(file)

    print model_json[u'outputs'][0][u'data'][u'concepts'][0][u'value']

    if (toast_counter < 3 and float(model_json[u'outputs'][0][u'data'][u'concepts'][0][u'value']) > .48):
        toast_counter = toast_counter + 1
	print ("toast done is true")
	print (toast_counter)
    if (toast_counter >= 3):
	toast_done = True
	print ("Toast RIP")
	break
    else:
	print ("toast done is false")
	continue
    
    print (toast_perfect)
    toast_perfect = model_json[u'outputs'][0][u'data'][u'concepts'][0][u'value']
    print ("\n")


client = TwilioRestClient(account='AC24b3c0ad866586038e4f5ca818ae30ed',token='3bab3d6d5bef27855cfb5bada3c39346')
client.messages.create(to="+14077583284",from_="+14079019282", body="TOAST")
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.LOW)

time.sleep(1)
GPIO.output(2,GPIO.HIGH)
GPIO.cleanup()

