#!/usr/bin/env python
# encoding: utf-8
"""
porch.py - a place for bees to fan their hives

Created by Dave Williams on 2014-06-24
"""

import bee
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters, a temporary storage location
PORCH_X = 300          # porch width, 30cm
PORCH_Y = 500          # porch length, 50cm
ENTRANCE_WIDTH = 10    # width, located in center
STATIONARY_BEE_N = 20  # number of still bees
WALKING_BEE_N = 20     # number of walking bees at a time


class Porch(object):
    def __init__(self):
        """Construct the porch.

        The porch is a flat area outside the hive entrance. This contains 
        a representation of it that keeps track of the bees on it.
        """
        self.xlim = PORCH_X
        self.ylim = PORCH_Y
        self.entrance = ((0, PORCH_X/2-ENTRANCE_WIDTH/2),
                         (0, PORCH_X/2+ENTRANCE_WIDTH/2))
        # create self.stationary and self.walking pops
        self.populate_bees(STATIONARY_BEE_N, WALKING_BEE_N)

    def populate_bees(self, stationary_bees, walking_bees):
        """Instantiate the bees which will sit/walk on the porch."""
        random = np.random.uniform
        limits = (self.xlim - bee.BEE_SIZE[0], self.ylim - bee.BEE_SIZE[1])
        rand_xy = lambda: (random(0, limits[0]), random(0, limits[1]))
        new_stationary = lambda: bee.Bee(self, rand_xy(), True)
        new_walking = lambda: bee.Bee(self, rand_xy(), False)
        self.stationary = [new_stationary() for i in range(stationary_bees)]
        self.walking = [new_walking() for i in range(walking_bees)]

    def collision_check(self):
        pass

    def get_entrance(self):
        """Return the center location of the hive entrance."""
        return (self.entrance[0][1], 
                np.mean((self.entrance[0][0], self.entrance[1][0])))

    def get_edges(self):
        """Return the boundaries of the porch (x,y)."""
        return (self.xlim, self.ylim)

    def update_bees(self):
        """Move the bees along"""
        for b in self.stationary + self.walking:
            b.update_location()

    def porch_array(self):
        """Produce an array image of the porch with the bees on it"""
        porch_img = np.zeros((PORCH_Y, PORCH_X))
        for b in self.stationary + self.walking:
            bl = b.loc
            bi = b.show_bee()[:,:,0]
            porch_img[bl[1]:bl[1]+bi.shape[1], bl[0]:bl[0]+bi.shape[0]] += bi
        return porch_img

