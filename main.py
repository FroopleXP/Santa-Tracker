import time
import Adafruit_SSD1306
import threading
import RPi.GPIO as GPIO
import subprocess

from datetime import datetime

# Importing tracker
from tracker import SantaTracker

# Importing screens
from screens.screen_tracker import TrackerScreen
from screens.screen_calendar import CalendarScreen
from screens.screen_status import StatusScreen
from screens.screen_shutdown import ShutdownScreen

# Importing display
from display import TrackerDisplay

# Display settings
DISPLAY_I2C_ADDR = 0x3c
DISPLAY_RESET = 24

# Tracking settings
TRACKER_OFFSET = 3918270000

# App state
TIME_START_TRACKER = int(datetime.strptime("24/12/{} 10:00:00".format(datetime.now().year), "%d/%m/%Y %H:%M:%S").timestamp())

# Creating OLED display
display = Adafruit_SSD1306.SSD1306_128_64(rst=DISPLAY_RESET, i2c_address=DISPLAY_I2C_ADDR)
display.begin()

# Creating instance of Santa Tracker
tracker = SantaTracker(TRACKER_OFFSET)

# Creating a display
tracker_display = TrackerDisplay()
tracker_display.register(name="tracker", screen=TrackerScreen(tracker))
tracker_display.register(name="calendar", screen=CalendarScreen(TIME_START_TRACKER))
tracker_display.register(name="status", screen=StatusScreen())
tracker_display.register(name="shutdown", screen=ShutdownScreen())

# Setting up button int.
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, lambda c : tracker_display.next(), bouncetime=300)

# Power switch
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(24, GPIO.FALLING, lambda c : tracker_display.show("shutdown"), bouncetime=300)

while True:
    try:
        # Update display
        display.image(tracker_display.render())
        display.display()
        
        # Block exec to reduce CPU usage
        time.sleep(.3)
        
    except KeyboardInterrupt:
        break
        
GPIO.cleanup()
    



        

