import subprocess
import threading

from . screen import Screen
from PIL import Image, ImageFont, ImageDraw

class ShutdownScreen(Screen):
    
    def __init__(self, width=128, height=64):
        
        self.__width = width
        self.__height = height
        
        # Creating shutdown timer
        self.__timer = threading.Timer(5, self.__shutdown)
        self.__timer_has_ran = False
        
        # Creating image
        self.__lg_font = ImageFont.truetype("fonts/liberation.ttf", 16)
        self.__sm_font = ImageFont.truetype("fonts/minecraftia.ttf", 8)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)
                
    def __clear_frame(self):
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
    
    def __shutdown(self):
        self.__timer_has_ran = True
        subprocess.call(["shutdown", "-h", "now"], shell=False)
    
    def render(self):
    
        self.__clear_frame()
        
        self.__frame.text((6, 4), "Shutting down", font=self.__sm_font, fill=1)
        self.__frame.multiline_text((6, 16), "System is shutting down.\nPlease do not unplug\nuntil red lamp is\nturned off.", font=self.__sm_font, fill=1, spacing=-4)
        
        # Start shutdown timer
        if (not self.__timer.is_alive() and not self.__timer_has_ran): self.__timer.start()
            
        return self.__image
