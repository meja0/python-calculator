
import pathlib

from PIL import Image, ImageDraw, ImageFont


HORSE = r"""
            _|\ _/|_,
           ,((\\``-\\\\_
         ,(())      `))\
       ,(()))       ,_ \
      ((())'   |        \
      )))))     >.__     \
      ((('     /    `-. .c|   %s
              /        `-`'
"""

HORSE_LOCATION = pathlib.Path() / 'horse_mof.png'

def enhorseify(value):
    with Image.open(HORSE_LOCATION) as im:
        font = ImageFont.truetype("Arial.ttf", size=32)
        draw = ImageDraw.Draw(im)
        draw.text((80, 200), text=str(value), fill=(0, 0, 0))
        im.show()


def horse(x, y, z):
    return "HORSE"