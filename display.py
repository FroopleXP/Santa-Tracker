from screens import Screen
import RPi.GPIO as GPIO

class TrackerDisplay:
    
    def __init__(self, width=128, height=64):
        
        self.__width = width
        self.__height = height
        
        # Registering screens
        self.__screen_idx = 0
        self.__max_idx = 0
        self.__screens = []
    
    def render(self):
        return self.__screens[self.__screen_idx].render()
    
    def prev(self):
        self.__screen_idx = self.__max_idx if self.__screen_idx - 1 < 0 else self.__screen_idx - 1

    def next(self):
        self.__screen_idx = 0 if self.__screen_idx + 1 > self.__max_idx else self.__screen_idx + 1
    
    def registerscreen(self, screen):
        self.__screens.append(screen)
        self.__max_idx = len(self.__screens) - 1
        
        

