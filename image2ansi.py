#!/usr/bin/env python3
import argparse
import math
from textwrap import dedent

from PIL import Image
from x256 import x256

# Maximum width for the output in columns
OUTPUT_MAX_WIDTH = 80
ANSI_RESET = '\x1b[0m'


def convert_to_ansi(input_stream, output_stream):
    image = Image.open(input_stream)
    image = image.convert('RGBA')
    output = ''

    # Calculate relative pixel size based on bounding box
    # See: https://github.com/dfrankland/image-xterm-loader/blob/master/src/index.js#L25
    dx = image.width / OUTPUT_MAX_WIDTH
    dy = 2 * dx
    # print("Image size:", image.width, image.height)
    # print("Relative pixel size:", dx, dy)
    # print(image.mode)

    # Start reading the image pixel-by-pixel, incrementing by the relative pixel size
    # We decrement the width by a single relative pixel size
    # to prevent reading out-of-bounds of the image.
    x, y = 0, 0
    while y < math.floor(image.height - dy):
        while x < math.floor(image.width - dx):
            x += dx
            pixel = image.getpixel((x, y))
            if pixel[3] > 0:
                # @TODO Refactor x256 core bits into a single file?
                ansi_colour = '\x1b[48;5;' + str(x256.from_rgb(pixel[0], pixel[1], pixel[2])) + 'm'
                output += f'{ansi_colour} {ANSI_RESET}'
            else:
                output += f' {ANSI_RESET}'

        # Next vertical row, reset horizontal index to 0
        x, y = 0, y + dy

        # Reset colors and force new row
        output = f"{output}{ANSI_RESET} \r\n"

    # Print output to stdout
    output_stream.write(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Convert any image format supported by pillow into a series of "pixels" using ANSI-escape codes',
        epilog='Note: Works best for relatively low-resolution images (Pokemon party/pokedex list sprites work really well)')
    parser.add_argument('input', type=argparse.FileType('rb'),
                        help='input file to convert', default='-')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        help='output file/stream', default='-')
    args = parser.parse_args()
    convert_to_ansi(args.input, args.output)
