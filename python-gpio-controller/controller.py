import RPi.GPIO as GPIO
import time, sys
from time import sleep

#Define input ports
PORT_FOB01=11 #Wireless remote used to activate/deactivate alarm 
PORT_PIR01=12 #Connected physical port 12 to a PIR
PORT_PIR02=13 #Connected physical port 13 to a PIR
PORT_UNUSED=15
PORT_UNUSED=16
PORT_UNUSED=18

#Define output ports
PORT_SIREN01=22

#An interrupt is called when PIR01 is triggered
def isrFOB01(channel):
	print('FOB01')
	if isArmed():
		disarm()
	else:
		arm()

#An interrupt is called when PIR01 is triggered
def isrPIR01(channel):
	if isArmed():
		updateStatus('PIR01','1')
		initSiren()
		updateStatus('PIR01','0')
	else:
		updateStatus('PIR01','1')
		print "PIR01 triggered but alarm is disarmed"
		sleep(2)
		updateStatus('PIR01','0')

#An interrupt is called when PIR01 is triggered
def isrPIR02(channel):
	if isArmed():
		updateStatus('PIR02','1')
		initSiren()
		updateStatus('PIR02','0')
	else:
		updateStatus('PIR02','1')
		print "PIR02 triggered but alarm is disarmed"
		sleep(2)
		updateStatus('PIR02','0')

def updateStatus(filename, state):
	f = open(filename,'w')
	f.write(state)
	f.close()

#Check wheter alarm is currently armed
def isArmed():
	f = open('isAlarmActivated','r')
	isArmed=f.read()
	f.close()
	if isArmed.find("1")==-1: 
		return False;
	else:
		return True;

#Arm the system 
def arm():
	print "Alarm Status - ***ARMED***"
	f = open('isAlarmActivated','w')
	f.write('1')
	f.close()
	sirenWarn()

#Disarm the system
def disarm():
	print "Alarm Status - ***DISARMED***"	
	f = open('isAlarmActivated','w')
	f.write('0')
	f.close()
	sirenWarn()
	sleep(0.3)	
	sirenWarn()

#Initiate Siren activation sequence
def initSiren():
	GPIO.remove_event_detect(PORT_PIR01)
	GPIO.remove_event_detect(PORT_PIR02)
	#Give a warning siren
	sirenWarn()
	print "Wait 5 seconds"
	sleep(5)
	#Check if still armed
	if isArmed() is False:
		print "Siren sequence stopped"
		GPIO.add_event_detect(PORT_PIR01,GPIO.FALLING, callback=isrPIR01 , bouncetime=200)
		GPIO.add_event_detect(PORT_PIR02,GPIO.FALLING, callback=isrPIR02 , bouncetime=200)
		return
	else:
		print "Siren still armed"
	sirenWarn()
	sleep(10)
	#Check if still armed
	if isArmed() is False:
		print "Siren sequence stopped"
		GPIO.add_event_detect(PORT_PIR01,GPIO.FALLING, callback=isrPIR01 , bouncetime=200)
		GPIO.add_event_detect(PORT_PIR02,GPIO.FALLING, callback=isrPIR02 , bouncetime=200)
		return
	else:
		print "Siren still armed"
	sirenActivate()
	GPIO.add_event_detect(PORT_PIR01,GPIO.FALLING, callback=isrPIR01 , bouncetime=200)
	GPIO.add_event_detect(PORT_PIR02,GPIO.FALLING, callback=isrPIR02 , bouncetime=200)

#Give a warning beep on Siren
def sirenWarn():
	print "Siren warning"
	GPIO.output(PORT_SIREN01,1)
	sleep(0.3)
	GPIO.output(PORT_SIREN01,0)

#Fully Activate the alarm
def sirenActivate():
	print "Siren is  Activated"
	GPIO.output(PORT_SIREN01,1)
	count=0
	while True:
		if isArmed():
			print "Still Activated"
		else:
			print "Siren sequence stopped"
			GPIO.output(PORT_SIREN01,0)
			return
		if count > 300 :
			print "Siren sequence stopped - 3 minutes passed"
			GPIO.output(PORT_SIREN01,0)
			return
		count=count+1
		print count
		sleep(1)

#=============================MAIN==================================
#We will use the physical port number
GPIO.setmode(GPIO.BOARD)  

GPIO.setup(PORT_FOB01 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_PIR01 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_PIR02 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PORT_SIREN01 , GPIO.OUT)

#Setup callback when pin 
GPIO.add_event_detect(PORT_FOB01,GPIO.FALLING, callback=isrFOB01 , bouncetime=200)
GPIO.add_event_detect(PORT_PIR01,GPIO.FALLING, callback=isrPIR01 , bouncetime=200)
GPIO.add_event_detect(PORT_PIR02,GPIO.FALLING, callback=isrPIR02 , bouncetime=200)

while True:
	try:
		print "I am Alive"
		sleep(300)
	except KeyboardInterrupt:
		print "Cleanup and exit", sys.exc_info()[0]
		#GPIO.output(PORT_SIREN01,0)
		GPIO.cleanup()
		break
#		sys.exit()
