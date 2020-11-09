from screens import Screen
import RPi.GPIO as GPIO

from animation import ScrollingText
from PIL import Image, ImageFont, ImageDraw

class CalendarScreen(Screen):
    
    def __init__(self, tracker, width=128, height=64):
        self.__width = width
        self.__height = height
        
        self.__number = 0
        
        # Creating image
        self.__font = ImageFont.truetype("fonts/liberation.ttf", 10)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)
    
    def __inc_number(self, channel):
        self.__number += 1
    
    def __clear_frame(self):
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
    
    def render(self):
        
        self.__clear_frame()
        
        self.__frame.multiline_text((4, 3), text="Number: {}".format(self.__number), font=self.__font, fill=1)
        
        return self.__image
        

