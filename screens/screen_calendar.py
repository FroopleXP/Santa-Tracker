import time

from datetime import datetime
from screens import Screen
from PIL import Image, ImageFont, ImageDraw

class CalendarScreen(Screen):
    
    def __init__(self, width=128, height=64):

        self.__count_to = int(datetime.strptime("24/12/{} 10:00:00".format(datetime.now().year), "%d/%m/%Y %H:%M:%S").timestamp())
        self.__width = width
        self.__height = height
        
        # Creating image
        self.__sm_font = ImageFont.truetype("fonts/minecraftia.ttf", 8)
        self.__lg_font = ImageFont.truetype("fonts/liberation.ttf", 32)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)

    def __clear_frame(self):
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
    
    def render(self):
        
        self.__clear_frame()
        
        days = int((self.__count_to - time.time()) / 86400)
        plural = "s" if days > 1 else ""
        
        self.__frame.multiline_text((4, 4), text="Countdown", font=self.__sm_font, fill=1)
        self.__frame.multiline_text((75, 20), text="Day{} 'til".format(plural), font=self.__sm_font, fill=1)
        self.__frame.multiline_text((75, 30), text="take off", font=self.__sm_font, fill=1)
        self.__frame.multiline_text((4, 16), text="{}".format(days), font=self.__lg_font, fill=1)
        
        return self.__image
        

