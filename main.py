import time
import Adafruit_SSD1306
import threading
import RPi.GPIO as GPIO

# Importing tracker
from tracker import SantaTracker

# Importing screens
from screens.screen_tracker import TrackerScreen
from screens.screen_calendar import CalendarScreen

# Importing display
from display import TrackerDisplay

# Display settings
DISPLAY_FREQ = 1 / 5
TRACKER_OFFSET = 3918270000

# Creating OLED display
display = Adafruit_SSD1306.SSD1306_128_64(rst=24)
display.begin()

# Creating instance of Santa Tracker
tracker = SantaTracker(TRACKER_OFFSET)

# Creating a display
tracker_display = TrackerDisplay()
tracker_display.register(name="tracker", screen=TrackerScreen(tracker))
tracker_display.register(name="calendar", screen=CalendarScreen())

# Setting up button int.
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.FALLING, lambda c : tracker_display.prev(), bouncetime=300)

while True:
    try:
        display.image(tracker_display.render())
        display.display()
        time.sleep(.3)
    except KeyboardInterrupt:
        break
        
GPIO.cleanup()
    



        

