import board
import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297

displayio.release_displays()

# For I2C
display_bus = displayio.I2CDisplay(board.I2C(), device_address=0x3D)

# Width, height border and rotation 
WIDTH = 128
HEIGHT = 128
ROTATION = 90
BORDER = 2

display = SH1107(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
    rotation=ROTATION,
)

# Making my first group to which ill keep appending
splash = displayio.Group()
display.show(splash)

#drawing the 1st frame 128x128 black square bitmap and then my first tile grid and then append/draw over my group splash
frame_1 = displayio.Bitmap(WIDTH, HEIGHT, 1)
palette_1 = displayio.Palette(1)
palette_1[0] =0xFFFFFF #WHITE

bg_sprite = displayio.TileGrid(frame_1, pixel_shader=palette_1, x=0, y=0)
splash.append(bg_sprite)

#drawing frame 2 a black square 
frame_2 = displayio.Bitmap(32, 32, 1)
palette_2 = displayio.Palette(1)
palette_2[0] = 0x000000 #BLACK

inner_sprite =displayio.TileGrid(frame_2, pixel_shader=palette_2, x=48, y=48)
splash.append(inner_sprite)


while True:
    pass