#! /usr/bin/env python3
# virtual assistant <mohini>

import os
import datetime as dt
import pytz
import pyttsx3
import pyaudio

# #speech to text
# text = []

# def listen():
# 	audi = pyaudio.pyaudio()
# 	lis = audi.open(format=pyaudio.paInt16, channels=2, rate=44100, output=True, frames_per_buffer=1024)
# 	data = lis.read(1024)
# 	data.append(text)

# print(text)

#text to speech module
def speak(self):
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')
	vol = engine.getProperty('volume')
	engine.setProperty('rate', rate-10)
	engine.setProperty('volume', vol+1.0)
	engine.say(str(self))
	engine.runAndWait()

#align the timezones using pytz
gmt = pytz.timezone('Etc/GMT')
ist = pytz.timezone('Asia/Kolkata')
jst = pytz.timezone('Japan')

#take input from user and decorate
ctime = input("\n**************Time Convertor*******************\n\nEnter Time(eg: 23:45): ")
ctz = input("\nTimezone is ist (specify \"gmt/jst\" if otherwise): ")
if str(ctz) == "gmt":
	tz = gmt
elif str(ctz) == "jst":
	tz = jst
else:
	tz = ist
cformat = dt.date.today().strftime("%d-%m-%Y") + " " + str(ctime) + ":00"
dformat = dt.datetime.strptime(cformat, "%d-%m-%Y %H:%M:%S")

#convert the current time in different tz's and decorate using dt
stime = dt.datetime.now(gmt).strftime("%d-%m-%Y %H:%M:%S GMT")
smani = dt.datetime.now(ist).strftime("%d-%m-%Y %H:%M:%S IST")
sjikan = dt.datetime.now(jst).strftime("%d-%m-%Y %H:%M:%S JST")

time = tz.localize(dformat)
ctime = time.astimezone(gmt).strftime("%d-%m-%Y %H:%M:%S GMT")
cmani = time.astimezone(ist).strftime("%d-%m-%Y %H:%M:%S IST")
cjikan = time.astimezone(jst).strftime("%d-%m-%Y %H:%M:%S JST")

#print the time in different tz's
print("\ncurrent date & time")
print(stime,"\n",smani,"\n",sjikan)
print("\nyour date & time")
print(ctime,"\n",cmani,"\n",cjikan)

speak("For the Provided Input, the time would be "+ctime)
speak("and "+cmani)
speak("and "+cjikan)