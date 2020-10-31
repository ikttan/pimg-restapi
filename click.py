#!/usr/bin/python

from picamera import PiCamera
import requests
import base64

myUrl = 'http://<Your_Hostname_or_IP/API_Path>'
camera = PiCamera()

camera.capture('image.jpg')
encoded64 = base64.encodestring(open('image.jpg', 'rb').read())

response = requests.post(myUrl, data=encoded64, headers={'content-type':'image/jpeg'})
