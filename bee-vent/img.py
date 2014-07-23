#!/usr/bin/env python
# encoding: utf-8
"""
img.py - provide an interface to an image with extra functionality above PIL

Created by Dave Williams on 2014-06-23
"""

from PIL import Image
import numpy as np


class BeeImg(object):
    """In this class, rotation is stored as an angle by which the bee is
    rotated counter clockwise from facing up the screen. The image is only
    rotated on being displayed as repeated rotations of an image degrade it;
    that is, if we were to repeatedly apply rotations to the image, rather 
    than rotating it only when it's displayed, the image would lose sharpness.
    """
    def __init__(self, img_loc = './bee.png'):
        self._img = Image.open(img_loc)
        self._rotation = 0

    def rotate(self, deg = 0):
        """Rotate the image to the specified angle."""
        self._rotation = deg

    def rotate_by(self, deg = 0):
        """Rotate the image counter clockwise by X degrees."""
        self._rotation += deg  # to be able to reset

    def reset_rotation(self):
        """Rotate back to our original orientation."""
        self._rotation = 0

    def img(self):
        """Return the image as a PIL image instance."""
        return self._img.rotate(self._rotation)

    def array(self):
        """Return the image as a numpy array."""
        return np.array(self._img.rotate(self._rotation))

def new_bee_img():
    return BeeImg()
