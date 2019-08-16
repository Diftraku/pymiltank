#!/usr/bin/env python3
import argparse
from PIL import Image
from textwrap import dedent
import math
from x256 import x256

# Maximum width for the output in columns
OUTPUT_MAX_WIDTH = 80
ANSI_RESET = '\x1b[0m'

def convert_png(file):
    image = Image.open(file)
    image = image.convert('RGBA')
    output = ''

    # Calculate relative pixel size based on bounding box
    # See: https://github.com/dfrankland/image-xterm-loader/blob/master/src/index.js#L25
    dx = image.width / OUTPUT_MAX_WIDTH
    dy = 2 * dx
    # print("Image size:", image.width, image.height)
    # print("Relative pixel size:", dx, dy)
    # print(image.mode)

    # Read pixels from the image, incrementing by relative pixel size
    x, y = 0, 0
    while y < math.floor(image.height - dy):
        while x < math.floor(image.width - dx):
            x += dx
            pixel = image.getpixel((x, y))
            if pixel[3] > 0:
                ansi_colour = '\x1b[48;5;' + str(x256.from_rgb(pixel[0], pixel[1], pixel[2])) + 'm'
                output += f'{ansi_colour} {ANSI_RESET}'
            else:
                output += f' {ANSI_RESET}'
        # Reset after every row and force newline
        x, y = 0, y + dy
        output = f"{output}{ANSI_RESET} \r\n"
    # Dump the resulting "file"
    print(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert a PNG image into a series of "pixels" using ANSI-escape codes',
        epilog='Note: Works best for relatively low-resolution images (Pokemon party/pokedex list sprites work really well)')
    parser.add_argument('file', type=argparse.FileType('rb'), help='path to file to convert')
    args = parser.parse_args()
    convert_png(args.file)
