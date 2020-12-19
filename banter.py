#!/usr/bin/env python3

import sys,time
from PIL import Image
from color import closestColor

ASCIIWIDTH=80
COLORCHAR='\x03{},{}' # this will be String.format()'ted with two args
FILLER='.'

if len(sys.argv) < 2:
    raise Exception('you must supply an image')

im = Image.open(sys.argv[1], 'r')
width, height = im.size
pixel_values = list(im.getdata())

ipix = width // ASCIIWIDTH # // instead of / to devide with a round number

asciiHeight = height // ipix

for y in range(asciiHeight):
    line = []
    lastColor=69420

    for x in range(ASCIIWIDTH):
        color = closestColor(pixel_values[width*(y*ipix)+(x*ipix)])
        if color == lastColor:
            colorcode = ''
        else:
            colorcode =COLORCHAR.format(color, color)
        line.append(colorcode+FILLER)
        lastColor=color

    print(''.join(line))
    if len(sys.argv) > 2:
        time.sleep(float(sys.argv[2]))
