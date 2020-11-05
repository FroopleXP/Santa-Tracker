import RPi.GPIO as GPIO
import time

def cb(channel):
    if (channel == 23):
        print("Left")
    
    if (channel == 24):
        print("Right")

def cb2(channel):
    print("alled")

GPIO.setmode(GPIO.BCM)

# Pin 23 setup
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
GPIO.add_event_detect(23, GPIO.FALLING, cb, bouncetime=300)

# Pin 24 setup
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, cb, bouncetime=300)

last_poll_time = time.time();
interval = 1 / .5

GPIO.cleanup()
    
