from screens.screen import Screen
import RPi.GPIO as GPIO

class TrackerDisplay:
    
    def __init__(self, width=128, height=64):
        self.__width = width
        self.__height = height
        
        # Screen tracking
        self.__default_screen = None
        self.__current_screen = None
        self.__screens = {}
    
    def render(self) -> None:
        if (not len(self.__screens)): return # Do nothing if no screens are registered
        screen = self.__current_screen or self.__default_screen # Default back to default screen is current screen isn't set
        return self.__screens.get(screen).render()
    
    def prev(self) -> None:
        screen_list = list(self.__screens)
        for idx, value in enumerate(screen_list):
            if (value == self.__current_screen):
                if (not idx): self.__current_screen = screen_list[len(screen_list) - 1]
                else: self.__current_screen = screen_list[idx - 1]
                break

    def next(self) -> None:
        screen_list = list(self.__screens)
        for idx, value in enumerate(screen_list):
            if (value == self.__current_screen):
                if (idx + 1 > len(self.__screens) - 1): self.__current_screen = screen_list[0]
                else: self.__current_screen = screen_list[idx + 1]
                break
                    
    def show(self, name) -> None:
        if (not name in self.__screens): return # Do nothing if screen isn't registered
        self.__current_screen = name
    
    def register(self, name, screen, default=False) -> None:
        if (not len(self.__screens)): default = True # If this is the first screen, set as default
        self.__screens[name] = screen
        if (default): self.__default_screen = self.__current_screen = name
        
        

