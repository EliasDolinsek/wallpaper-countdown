import datetime
import time
import ctypes
import os

from PIL import Image, ImageDraw, ImageFont

WALLPAPER_IMG_NAME = "wallpaper.png"
SPI_SET_DESK_WALLPAPER = 20

countdown_datetime = datetime.datetime.now() + datetime.timedelta(hours=1)
event_name = "Some event"


def set_wallpaper_image():
    path = os.path.abspath(WALLPAPER_IMG_NAME)
    ctypes.windll.user32.SystemParametersInfoA(SPI_SET_DESK_WALLPAPER, 0, path, 0)


def create_and_save_wallpaper(remaining_seconds, display_name):
    img = Image.new("RGB", (1920, 1080), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    event_name_font = ImageFont.truetype("OpenSans-Regular.ttf", size=50)
    countdown_font = ImageFont.truetype("OpenSans-SemiBold.ttf", size=120)

    hours, remainder = divmod(remaining_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_text = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    countdown_text_width, countdown_text_height = draw.textsize(countdown_text, font=countdown_font)
    event_text_with, event_text_height = draw.textsize(display_name, font=event_name_font)

    event_name_x = img.width / 2 - event_text_with / 2
    countdown_x = img.width / 2 - countdown_text_width / 2

    event_name_y = img.height / 2 + event_text_height
    countdown_y = img.height / 2 - countdown_text_height / 1.5

    draw.text((event_name_x, event_name_y), display_name, fill=(0, 0, 0), font=event_name_font)
    draw.text((countdown_x, countdown_y), countdown_text, fill=(0, 0, 0), font=countdown_font)

    img.save("wallpaper.png")


while True:
    remaining_time = countdown_datetime - datetime.datetime.now()
    if remaining_time < datetime.timedelta(seconds=0):
        create_and_save_wallpaper(remaining_seconds=0, display_name=event_name)
        set_wallpaper_image()
        break
    else:
        create_and_save_wallpaper(remaining_seconds=remaining_time.seconds, display_name=event_name)
        set_wallpaper_image()
    time.sleep(1)
