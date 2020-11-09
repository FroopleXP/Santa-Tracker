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
#TRACKER_OFFSET = 0

# Creating OLED display
display = Adafruit_SSD1306.SSD1306_128_64(rst=24)
display.begin()

# Creating instance of Santa Tracker
tracker = SantaTracker(TRACKER_OFFSET)

# Creating a display
tracker_display = TrackerDisplay()
tracker_display.registerscreen(TrackerScreen(tracker))
tracker_display.registerscreen(CalendarScreen())

def updatescreen(screen): 
    display.image(screen)
    display.display()

while True:
    try:
        updatescreen(tracker_display.render())
        time.sleep(.3)
    except KeyboardInterrupt:
        break
        
GPIO.cleanup()
    



        

