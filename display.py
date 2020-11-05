from screens import Screen
import RPi.GPIO as GPIO

class TrackerDisplay:
    
    def __init__(self, width=128, height=64):
        
        self.__width = width
        self.__height = height
        
        # Registering screens
        self.__screen_idx = 0
        self.__screens = []
        
        # Registering interrupts
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)    
        GPIO.add_event_detect(23, GPIO.FALLING, self.__irq, bouncetime=300)
        
    def __irq(self, ctx):
        print(len(self.__screens))
        if ((self.__screen_idx + 1) < len(self.__screens)):
            self.__screen_idx += 1
        else:
            self.__screen_idx = 0
    
    def render(self):
        return self.__screens[self.__screen_idx].render()
        
    def registerscreen(self, screen):
        self.__screens.append(screen)
        
        

