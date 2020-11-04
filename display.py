from PIL import Image, ImageFont, ImageDraw
# Display
# DISP_WIDTH = 128
# DISP_HEIGHT = 64

# font = ImageFont.truetype("fonts/minecraftia.ttf", 8)
# display = Image.new("1", (DISP_WIDTH, DISP_HEIGHT))

# tracking_screen = ImageDraw.Draw(display)
# tracking_screen.multiline_text((4, 4), text=" - Santa Tracker - ", font=font, fill=1, align="center")
# tracking_screen.multiline_text((4, 16), "Loc: \n{}, {}\nDel.: {}\nStops: {}".format(curr_loc["city"], curr_loc["region"], curr_loc["presentsDelivered"], stops), font=font, fill=1, spacing=-4)

# display.save("tracking.png")

class TrackerDisplay:

    def __init__(self):

