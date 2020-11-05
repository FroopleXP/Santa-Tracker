from screens import Screen

from animation import ScrollingText
from tracker import SantaTracker
from PIL import Image, ImageFont, ImageDraw

class TrackerScreen(Screen):
    
    def __init__(self, tracker=SantaTracker(), width=128, height=64):
        self.__tracker = tracker
        self.__width = width
        self.__height = height
        
        # Creating image
        self.__font = ImageFont.truetype("fonts/liberation.ttf", 10)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)
        
        self.location_text = ScrollingText(
            "{}, {}".format(
                self.__tracker.getcurrentlocation()["city"],
                self.__tracker.getcurrentlocation()["region"]
            ),
            window_size=18
        )
        
        self.presents_delivered_text = ScrollingText(
            "{}".format(
                self.__tracker.getcurrentlocation()["presentsDelivered"],
            ),
            window_size=18
        )
        
        self.status_text = ScrollingText(
            "{}".format(
                self.__tracker.getcurrentstatus()["status"]
            ),
            window_size=18
        )
        
    def __clear_frame(self):
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
        
    def render(self):
        
        self.__clear_frame()
        
        self.__frame.multiline_text((4, 3), text="Santa Tracker", font=self.__font, fill=1)
        self.__frame.multiline_text((4, 16), text=self.location_text.render(), font=self.__font, fill=1)
        self.__frame.multiline_text((4, 30), text=self.status_text.render(), font=self.__font, fill=1)
        self.__frame.multiline_text((4, 44), text=self.presents_delivered_text.render(), font=self.__font, fill=1)
        
        return self.__image
        

