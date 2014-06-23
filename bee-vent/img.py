#!/usr/bin/env python
# encoding: utf-8
"""
img.py - provide an interface to an image with extra functionality above PIL

Created by Dave Williams on 2014-06-23
"""

from PIL import Image
import numpy as np


class BeeImg(object):
    def __init__(self, img_loc = './bee.png'):
        self.img = Image.open(img_loc)
        self._rotation = 0

    def rotate(self, deg = 0):
        """Rotate the image counter clockwise by X degrees."""
        self._rotation += deg  # to be able to reset
        self.img = self.img.rotate(deg)

    def reset_rotation(self):
        """Rotate back to our original orientation."""
        self.img = self.img.rotate(-self._rotation)
        self._rotation -= self._rotation

    def img(self):
        """Return the image as a PIL image instance."""
        return self.img

    def array(self):
        """Return the image as a numpy array."""
        return np.array(self.img)

def new_bee_img():
    return BeeImg()
