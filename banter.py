#!/bin/sh
''''exec /usr/bin/env python3 -u "$0" "$@" #'''
__doc__ = 'little script to make irc color art that will probably get you banned'
# whee, look at this sus shebang workaround to always cause
# unbuffered mode lol

import sys,time,argparse
from PIL import Image
from color import closestColor


def main(imgPath,delay,ASCIIWIDTH,COLORCHAR,FILLER):
    im = Image.open(imgPath, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())

    ipix = width // ASCIIWIDTH # // instead of / to devide with a round number

    asciiHeight = height // ipix // 2

    currentPixel = 0

    for y in range(asciiHeight):
        line = []
        lastColor=69420

        for x in range(ASCIIWIDTH):
            color = closestColor(pixel_values[width*(y*(ipix*2))+(x*ipix)])
            if color == lastColor:
                colorcode = ''
            else:
                colorcode =COLORCHAR.format(color, color)
            line.append(colorcode+(FILLER[currentPixel % len(FILLER)]))
            lastColor=color
            currentPixel+=1

        print(''.join(line))
        if delay:
            time.sleep(delay)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("banter")
    parser.add_argument("file")
    parser.add_argument("-d",metavar='delay',default=0)
    parser.add_argument("-w",metavar='width',default=80)
    parser.add_argument("--colorfmt",metavar='format',default='\\x03{},{}')
    parser.add_argument("--filler",metavar='filler',default='.')
    args = parser.parse_args()

    main(
            args.file,
            float(args.d),
            int(args.w),
            args.colorfmt.encode().decode('unicode_escape'),
            args.filler.encode().decode('unicode_escape')
            )
