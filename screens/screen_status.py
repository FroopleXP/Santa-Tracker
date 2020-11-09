import time

from . screen import Screen
from PIL import Image, ImageFont, ImageDraw

class StatusScreen(Screen):
    
    def __init__(self, width=128, height=64):
        
        self.__width = width
        self.__height = height
        
        # Creating image
        self.__sm_font = ImageFont.truetype("fonts/minecraftia.ttf", 8)
        self.__lg_font = ImageFont.truetype("fonts/liberation.ttf", 32)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)

    def __clear_frame(self) -> None:
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
    
    def render(self) -> Image:
        
        self.__clear_frame()
        
        self.__frame.multiline_text((4, 4), text="Status", font=self.__sm_font, fill=1)
        
        return self.__image
        

