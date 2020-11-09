from screens import Screen

from animation import ScrollingText
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from utils import human_format

class TrackerScreen(Screen):
    
    def __init__(self, tracker, width=128, height=64):
        
        # Display settings
        self.__tracker = tracker
        self.__width = width
        self.__height = height
        
        # Creating image
        self.__lg_font = ImageFont.truetype("fonts/liberation.ttf", 16)
        self.__sm_font = ImageFont.truetype("fonts/minecraftia.ttf", 8)
        self.__image = Image.new("1", (self.__width, self.__height))
        self.__frame = ImageDraw.Draw(self.__image)
        
        # Keep track of last location
        self.__last_location = None
        self.__location_str = None
                
    def __clear_frame(self):
        self.__frame.rectangle((0, 0, self.__width, self.__height), fill=0)
        
    def render(self):
        
        self.__clear_frame()
        
        location = self.__tracker.getCurrentLocation()
        presents = human_format(location.get("presentsDelivered"))
        stopover = location.get("stopover")
        curr_location = None
        
        # Printing local time
        local_time = datetime.fromtimestamp(int(self.__tracker.get_adj_time() / 1000)).strftime("%H:%M")
        self.__frame.text((95, 4), "[{}]".format(local_time), font=self.__sm_font, fill=1)
        
        if (stopover):
            departure = datetime.fromtimestamp(int(stopover.departure / 1000)).strftime("%H:%M")
            self.__frame.text((6, 4), "Location", font=self.__sm_font, fill=1)
            self.__frame.text((6, 48), "ETD: {} | D: {}".format(departure, presents), font=self.__sm_font, fill=1)
            curr_location = stopover
            
        else:
            eta = datetime.fromtimestamp(int(location.get("next").arrival / 1000)).strftime("%H:%M")
            self.__frame.text((6, 4), "Next stop", font=self.__sm_font, fill=1)
            self.__frame.text((6, 48), "ETA: {} | D: {}".format(eta, presents), font=self.__sm_font, fill=1)
            curr_location = location.get("next")
        
        # Checking if the location has changed
        if (self.__last_location == None or curr_location.id != self.__last_location.id):
            self.__last_location = curr_location
            self.__location_str = ScrollingText(text="{}, {}".format(self.__last_location.city, self.__last_location.region))
        
        self.__frame.text((6, 22), self.__location_str.render(), font=self.__lg_font, fill=1)
        
        return self.__image
        

