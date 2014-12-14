import RPi.GPIO as GPIO
import time, sys

#Define input ports
PORT_FOB01=11 #Wireless remote used to activate/deactivate alarm 
PORT_PIR01=12 #Connected physical port 12 to a PIR
PORT_PIR02=13 #Connected physical port 13 to a PIR
PORT_UNUSED=15
PORT_UNUSED=16
PORT_UNUSED=18

#Define output port
PORT_SIREN01=22

#An interrupt is called when PIR01 is triggered
def isrFOB01(channel):
	print('FOB01')

#An interrupt is called when PIR01 is triggered
def isrPIR01(channel):
	print('PIR01')

#An interrupt is called when PIR01 is triggered
def isrPIR02(channel):
	print('PIR02')

#We will use the physical port number
GPIO.setmode(GPIO.BOARD)  

#
GPIO.setup(PORT_FOB01 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_PIR01 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_PIR02 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_SIREN01 , GPIO.OUT)

#Setup callback when pin 
GPIO.add_event_detect(PORT_FOB01 , GPIO.RISING, callback=isrFOB01, bouncetime=3000)
GPIO.add_event_detect(PORT_PIR01 , GPIO.RISING, callback=isrPIR01, bouncetime=3000)
GPIO.add_event_detect(PORT_PIR02 , GPIO.RISING, callback=isrPIR02, bouncetime=3000)



while True:
    try:
        print "I am Alive"
        time.sleep(300)
    except KeyboardInterrupt:
        print "Bye"
        sys.exit()

