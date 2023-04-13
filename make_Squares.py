# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:59:40 2023

@author: Stephen
"""

from PIL import Image, ImageDraw

def generate_image(image_size, square_size, output_file):
    # Create a new image with a white background
    image = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(image)

    # Define square colors
    colors = ['red', 'green', 'blue', 'yellow']

    # Define square positions
    positions = [
        (0, 0),
        (image_size[0] - square_size, 0),
        (0, image_size[1] - square_size),
        (image_size[0] - square_size, image_size[1] - square_size)
    ]

    # Draw the squares
    for color, position in zip(colors, positions):
        draw.rectangle([position, (position[0] + square_size, position[1] + square_size)], fill=color)

    # Save the image to a file
    image.save(output_file)

if __name__ == "__main__":
    image_size = (400, 400)
    square_size = 50
    output_file = "squares_image.png"
    generate_image(image_size, square_size, output_file)
