#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import requests

def main():
    GPIO.setmode(GPIO.BCM)
    mypin = 23
    GPIO.setup(mypin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        time.sleep(0.01)
        state = GPIO.wait_for_edge(mypin, GPIO.RISING)
#        print('Edge detected')
#        print(GPIO.input(mypin))
        switch = GPIO.input(mypin)
        if switch:
#            print('I am turning off')
            req = requests.get('http://127.0.0.1:3000/api/v1/commands/?cmd=stop')
        else:
#            print('I am turning on')
            req = requests.get('http://127.0.01:3000/api/v1/commands/?cmd=playplaylist&name=rp_autoplay')
    GPIO.cleanup()


if __name__=="__main__":
    main()
