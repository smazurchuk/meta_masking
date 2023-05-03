# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 21:30:24 2023

This is a script to generate the images for the experiment.

It uses the shape of a circle and then

@author: Stephen
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



# Set the size of the square and the radius of the annuli
square_size = 15
circ_radius = 3
width = 1.5

# Make corners of square (This could probably be generalized)
corners = np.array([[-square_size, -square_size], [-square_size, square_size], 
                    [square_size, -square_size], [square_size, square_size]])
corners = corners / 2

# Create plots!

# Make mask
fig, ax = plt.subplots()
for corner in corners:
    annulus = matplotlib.patches.Annulus(corner, circ_radius,
                                         width=width,fc='gray')
    ax.add_patch(annulus)
    
# Set the limits of the plot
ax.set_xlim(-square_size, square_size)
ax.set_ylim(-square_size, square_size)
# Make axes ratio equal
plt.gca().set_aspect('equal')
# Remove axis
plt.axis('off')
# Save the output as a PNG file
plt.savefig('imgs/mask.png', dpi=300, transparent=True, bbox_inches='tight')

# Make fills
for i, corner in enumerate(corners):
    fig, ax = plt.subplots()
    annulus = plt.Circle(corner, circ_radius-width, 
                         ec='None',fc='gray',
                         linewidth=12)
    ax.add_patch(annulus)
    # Set the limits of the plot
    ax.set_xlim(-square_size, square_size)
    ax.set_ylim(-square_size, square_size)
    # Make axes ratio equal
    plt.gca().set_aspect('equal')
    # Remove axis
    plt.axis('off')
    # Save the output as a PNG file
    plt.savefig(f'imgs/{i+1}_stim.png', dpi=300, transparent=True,bbox_inches='tight')