import time
from animation import ScollingText
from tracker import SantaTracker

from PIL import Image, ImageFont, ImageDraw

tracker = SantaTracker()

time_offset = 4374420000

# Display
DISP_WIDTH = 128
DISP_HEIGHT = 64

font = ImageFont.truetype("fonts/minecraftia.ttf", 8)

disp_freq = 10
last_loc_id = None
loc_txt = None
last_time = time.time()
interval = 1 / disp_freq

while True:

    if (time.time() - last_time >= interval): # Set framerate
        last_time = time.time()

        # Checking if the location has changed
        curr_loc = tracker.getcurrentlocation(time_offset)
        if (last_loc_id == None or curr_loc["id"] != last_loc_id):
            last_loc_id = curr_loc["id"]
            loc_txt = ScollingText("{}, {}".format(curr_loc["city"], curr_loc["region"]), window_size=12)

        display = Image.new("1", (DISP_WIDTH, DISP_HEIGHT))
        tracking_screen = ImageDraw.Draw(display)
        tracking_screen.text((4, 16), "Loc: {}".format(loc_txt.render()), font=font, fill=1, spacing=-4)

        display.save("tracking.png")




