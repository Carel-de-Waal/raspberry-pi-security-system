from RPIO import PWM 
from time import sleep
import time
import atexit
from bottle import route, run, static_file ,post

#=======================Web-Server=======================
@route('/')
def static_main():
    return static_file('main.html' , root='./static/')

@route('/cam01_script.js')
def static_main():
    return static_file('cam01_script.js' , root='./static/')

@route('/servo_script.js')
def static_main():
    return static_file('servo_script.js' , root='./static/')

@post('/servo_up')
def servo_up():
	move('up')

@post('/servo_down')
def servo_down():
	move('down')

@post('/servo_left')
def servo_left():
	move('left')

@post('/servo_right')
def servo_right():
	move('right')

@post('/is_armed')
def isArmed():
	f = open('../python-gpio-controller/isAlarmActivated','r')
	isArmed=f.read()
	f.close()
	if isArmed.find("1")==-1: 
		return 'Disarmed';
	else:
		return 'Armed';

#======================Servo==========================
PAN_PIN = 19
TILT_PIN = 16

# This function maps the angle we want to move the servo to, to the needed PWM value
def angleMap(angle):
	return int((round((1950.0/180.0),0)*angle) +550)

# Cleanup any open objects
def cleanup():
    servo.stop_servo(PAN_PIN)
    servo.stop_servo(TILT_PIN)


def move(direction):
    # Choose the direction of the request
    if direction == 'left':
	    # Increment the angle by 10 degrees
        na = pins[PAN_PIN]['angle'] + 10
        # Verify that the new angle is not too great
        if int(na) <= 180:
            # Change the angle of the servo
            servoPan.set_servo(PAN_PIN, angleMap(na))
            # Store the new angle in the pins dictionary
            pins[PAN_PIN]['angle'] = na
        return str(na) + ' ' + str(angleMap(na))
    elif direction == 'right':
        na = pins[PAN_PIN]['angle'] - 10
        if na >= 0:
            servoPan.set_servo(PAN_PIN, angleMap(na))
            pins[PAN_PIN]['angle'] = na
        return str(na) + ' ' + str(angleMap(na))
    elif direction == 'up':
        na = pins[TILT_PIN]['angle'] + 10
        if na <= 180:
            servoTilt.set_servo(TILT_PIN, angleMap(na))
            pins[TILT_PIN]['angle'] = na
        return str(na) + ' ' + str(angleMap(na))
    elif direction == 'down':
        na = pins[TILT_PIN]['angle'] - 10
        if na >= 0:
            servoTilt.set_servo(TILT_PIN, angleMap(na))
            pins[TILT_PIN]['angle'] = na
        return str(na) + ' ' + str(angleMap(na))

# Function to manually set a motor to a specific pluse width

def manual(motor,pulsewidth):
    if motor == "pan":
        servoPan.set_servo(PAN_PIN, int(pulsewidth))
    elif motor == "tilt":
        servoTilt.set_servo(TILT_PIN, int(pulsewidth))
    return "Moved"

# Create a dictionary called pins to store the pin number, name, and angle
pins = {
    PAN_PIN : {'name' : 'pan', 'angle' : 90},
    TILT_PIN : {'name' : 'tilt', 'angle' : 90}
    }

# Create two servo objects using the RPIO PWM library
servoPan = PWM.Servo()
servoTilt = PWM.Servo()

# Setup the two servos and turn both to 90 degrees
#servoPan.set_servo(PAN_PIN, angleMap(90))
#servoPan.set_servo(TILT_PIN, angleMap(90))

run(host='0.0.0.0', port=9977, debug=True)
