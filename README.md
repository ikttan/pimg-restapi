# Raspberry Pi image capture and send to server via RestAPI

A basic set of Python scripts to capture image on a Raspberry Pi and send it to a server via RestAPI.  This documentation comprises of the following parts

- Raspberry Pi OS and headless setup
- Installation of pip, picamera and requests libraries
- Python script to capture image, encode and send via HTTP requests
- crontab settings
- Python/Flask script for RestAPI

This repository doesn't intent to provide advance RestAPI setup, such as using JWT nor database driven.  It serves as a starter for those wanting to start somewhere.

## Raspberry Pi OS (Raspbian) and headless setup

### headless

### SSH

~~~
ssh pi@<pi_IP_number>
~~~

pi:raspberry

## Installation of pip, picamera and requests library

Should already have python installed

~~~
sudo apt-get install python-pip
sudo pip install picamera
sudo pip install requests
~~~

## Python script to capture image, encode and send via HTTP requests

~~~
#!/usr/bin/python

import picamera
import requests
import base64

~~~

## crontab settings

### Understanding crontab


## Python/Flask script for RestAPI

On the server, not on the Pi, you will also need to have the right libraries.  For image processing, you may want to use OpenCV and you can install it using

~~~
sudo pip install python-opencv
~~~


~~~
~~~
