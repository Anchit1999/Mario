'''move_bar.py'''
from board import BOARD
from config import BAR

class MovingBar():
    '''Code for moving bar'''
    def __init__(self, vel, xps, yps, lgt):
        self.vel = vel
        self.xps = xps
        self.yps = yps
        self.lgt = lgt
        self.tym = 0
    @classmethod
    def make_bar(cls, xps, yps, lgt):
        '''create bar'''
        # BOARD.mat[xps][yps-1]=' '
        for i in range(yps, yps + lgt):
            BOARD.mat[xps][i] = BAR

    def move(self, i=None):
        '''move bar'''
        if BOARD.checkstar(self.xps, self.yps + self.lgt + 1) == 1 and self.vel > 0 and i is None:
            self.vel = -self.vel
        if BOARD.checkstar(self.xps, self.yps - 2) == 1 and self.vel < 0:
            self.vel = -self.vel


BLIST = []
BLIST.append(MovingBar(1, 26, 202, 5))
