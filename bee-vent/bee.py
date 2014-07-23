#!/usr/bin/env python
# encoding: utf-8
"""
bee.py - provides the behavior and logic for a single bee

Created by Dave Williams on 2014-06-23
"""

import img
import numpy as np


# Simulation parameters, a temporary storage location
SIDLE_STOP = 0.2     # 20% chance of stopping sidling
SIDLE_BY = 1.0       # distance to sidle when sidling
HEAD_NOISE = 10      # standard deviation (in deg) of heading noise
WALK_MEAN = 2        # the mean distance to walk each turn
WALK_NOISE = 0.2     # the noise in the walking distance
BEE_SIZE = (16, 16)  # size of the bee image, once loaded


class Bee(object):
    def __init__(self, porch, location, stationary=True):
        """Create a bee, just like that.

        Takes:
            porch - the porch the bee is located on
            location - the (x,y) location of the bee on the porch
            stationary - if the bee's standing still (True)
        Gives:
            None
        """
        self.porch = porch
        self.stationary = stationary
        self.sidling = False  # something only stationary bees do
        self.img = img.new_bee_img()
        self.loc = location
        self.get_goal()  # set self.head

    def show_bee(self):
        """Give a matrix of the bee's image on the current heading."""
        dx, dy = np.subtract(self.head, self.loc)
        angle = 3*np.pi/2 - np.arctan2(dy, dx)
        self.img.rotate(np.degrees(angle))
        return self.img.array()

    def get_goal(self):
        """For now, just head to the entrance.

        Takes: 
            None
        Gives:
            head: the (x,y) coordinates the bee is heading towards
        """
        if self.stationary:
            self.head = (self.loc[0], 0)
        else:
            self.head = self.porch.get_entrance()
        return self.head

    def update_location(self):
        """Get a move on, or not, depending on the bee.
        
        Takes:
            None
        Gives:
            new_loc: the bee's updated (x,y) location
        """
        if self.stationary:
            # Stand still or sidle to the side
            if self.sidling is False:
                return self.loc  # stationary bee sits still for now
            elif self.sidling == 'Left':
                self.loc = (self.loc[0] - SIDLE_BY, self.loc[1])
                if SIDLE_STOP > np.random.rand():  # chance to stop
                    self.sidling = False
            elif self.sidling == 'Right':
                self.loc = (self.loc[0] + SIDLE_BY, self.loc[1])
                if SIDLE_STOP > np.random.rand():
                    self.sidling = False
        else:
            # Head towards the light^h^h^h^h^h heading, little bee
            dx, dy = np.subtract(self.head, self.loc)
            dist_to_goal = np.hypot(dx, dy)
            walk_this_much = np.random.normal(WALK_MEAN, WALK_NOISE)
            scale = walk_this_much/dist_to_goal
            self.loc = np.add(self.loc, (dx*scale, dy*scale))
        #TODO: check edges, coerce back to on porch if passed or wrap if
        # entrance is hit
        return self.loc

        def collide(self, side):
            """Bump a bee, from the Left or the Right.
            
            Takes:
                side: 'Left' or 'Right', the side the bee got bumped towards
            Gives:
                None
            """
            if self.stationary:
                self.sidling = side

