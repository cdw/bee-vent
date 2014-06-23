#!/usr/bin/env python
# encoding: utf-8
"""
bee.py - provides the behavior and logic for a single bee

Created by Dave Williams on 2014-06-23
"""

import img
import numpy as np
import matplotlib.pyplot as plt


## Simulation parameters, a temporary storage location
SIDLE_STOP = 0.2  # 20% chance of stopping sidling
HEAD_NOISE = 10   # standard deviation (in deg) of heading noise

class Bee(object):
    def __init__(self, porch, location, stationary = True):
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
        self.img = img.bew_bee_img()
        self.loc = location
        self.get_goal()  # set self.head

    def get_goal(self):
        """For now, just head to the entrance.
        
        Takes: 
            None
        Gives:
            goal: the (x,y) coordinates the bee is heading towards
        """
        self.head = porch.get_entrance()
        return self.head

    def update_location(self):
        """Get a move on, or not, depending on the bee.
        
        Takes:
            None
        Gives:
            new_loc: the bee's updated (x,y) location
        """
        if self.stationary:
            if self.sidling is False:
                return self.loc # stationary bee sits still for now
            elif self.sidling == 'Left':
                self.loc = (self.loc[0] - 1, self.loc[1])
                if SIDLE_STOP > np.random.rand():
                    self.sidling = False
            elif self.sidling == 'Right':
                self.loc = (self.loc[0] + 1, self.loc[1])
                if SIDLE_STOP > np.random.rand():
                    self.sidling = False
        else:
            #Head towards the light^h^h^h^h^h heading, little bee
            # TODO: Continue from here



