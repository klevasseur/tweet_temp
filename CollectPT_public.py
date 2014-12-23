#!/usr/bin/env python2.7  
#  by Ken Levasseur  http://home.comcast.net/~kmlevasseur/
#  building on work by Alex Eames http://raspi.tv/?p=5908 

#  This script presumes a serial connection to an Arduino (mine is an Uno) that is 
#  collecting pressure/temperature data.  My setup uses an MPL115A2 - I2C 
#  Barometric Pressure/Temperature Sensor (https://www.adafruit.com/product/992)

import tweepy  
import sys  
import os
import time
import datetime
import re
import serial



def tweettemp(filename):
# Consumer keys and access tokens, used for OAuth  
	consumer_key = 'insert_your_key'  
	consumer_secret = 'insert_your_secret'  
	access_token = 'insert_your_token'  
	access_token_secret = 'insert_your_token_secret'  
#  OAuth process, using the keys and tokens  
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
	auth.set_access_token(access_token, access_token_secret)  
	api = tweepy.API(auth)  
	time.sleep(10)	
	ser = serial.Serial('/dev/ttyACM0', 9600)
	items=ser.readline().split()
	datestring=datetime.datetime.now().ctime()
	tweet_text=datestring+": weather in My_location: "+items[1]+"F, "+items[0]+" inHg. #RaspberryPi"
	api.update_status(tweet_text)
	f = open(filename, 'a')
	f.write(str([datestring]+items))
	f.write('\n')
	f.close()
	

def main():

# Creation of the actual interface, using authentication  
	if len(sys.argv)>=2:
		args = sys.argv[1:]
		tweettemp(args[0])
	else:
		print 'argument:   file for collecting data'

if __name__ == '__main__':
	main()

  
