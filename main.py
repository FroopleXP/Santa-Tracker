import time
import RPi.GPIO as GPIO
import threading
import board
import busio
import adafruit_ssd1306

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

# Tracking settings
TIME_START_TRACKER = int(datetime.strptime("24/12/{} 10:00:00".format(datetime.now().year), "%d/%m/%Y %H:%M:%S").timestamp())

# Create the I2C Display
display = adafruit_ssd1306.SSD1306_I2C(128, 64, busio.I2C(board.SCL, board.SDA))

# Creating instance of Santa Tracker
tracker = SantaTracker()

# Creating a display
tracker_display = TrackerDisplay()
tracker_display.register(name="tracker", screen=TrackerScreen(tracker))
tracker_display.register(name="calendar", screen=CalendarScreen(TIME_START_TRACKER))
tracker_display.register(name="shutdown", toggleable=False, screen=ShutdownScreen())

# Buttons
BTN_NEXT_SCREEN = 24
BTN_PWR_DOWN = 23

# Setting GPIO mode
GPIO.setmode(GPIO.BCM)

# Next screen toggle
GPIO.setup(BTN_NEXT_SCREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BTN_NEXT_SCREEN, GPIO.FALLING, lambda c : tracker_display.next(), bouncetime=300)

# Power switch
GPIO.setup(BTN_PWR_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BTN_PWR_DOWN, GPIO.FALLING, lambda c : tracker_display.show("shutdown"), bouncetime=300)

def main():
    while True:
        try:
            # Update display
            display.image(tracker_display.render())
            display.show()
            
            # Block exec to reduce CPU usage
            time.sleep(.3)
            
        except KeyboardInterrupt:
            break
    GPIO.cleanup()
    
if __name__ == "__main__":
    main()

    



        

