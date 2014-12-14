import RPi.GPIO as GPIO
import time, sys

def isrPIR01(channel):
	print('Pin %s triggerred'%channel)

#We will use the physical port number
GPIO.setmode(GPIO.BOARD)  

GPIO.setup(11 , GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup callback when pin 
GPIO.add_event_detect(11 , GPIO.RISING, callback=isrPIR01, bouncetime=3000)


while True:
    try:
        print "I am Alive"
        time.sleep(300)
    except KeyboardInterrupt:
        print "Bye"
        sys.exit()

