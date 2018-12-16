'''flag.py'''
from board import BOARD

class Flag():
    '''Flag before the castle'''
    def __init__(self):
        self.vel = 1
        self.xps = 10
        self.first = 0
    @classmethod
    def print_on_board(cls, xps, yps=None):
        '''print flag'''
        yps = 502
        BOARD.mat[xps][yps] = '.'
        BOARD.mat[xps + 1][503] = '.'
        BOARD.mat[xps][503] = '.'
        BOARD.mat[xps + 2][504] = '.'
        BOARD.mat[xps + 1][504] = '.'
        BOARD.mat[xps][504] = '.'

        BOARD.mat[25 + 10 - xps][506] = '-'
        BOARD.mat[25 + 10 - xps][507] = '-'
        BOARD.mat[25 + 10 - xps][508] = '-'
        BOARD.mat[23 + 10 - xps][506] = '-'
        BOARD.mat[23 + 10 - xps][507] = '-'
        BOARD.mat[23 + 10 - xps][508] = '-'
        BOARD.mat[24 + 10 - xps][508] = '|'
        BOARD.mat[24 + 10 - xps][507] = '*'
        BOARD.mat[24 + 10 - xps][506] = '*'
        for i in range(10, 26):
            BOARD.mat[i][505] = '*'

    def move(self, k):
        '''movement of the flag'''
        if self.xps < 10 + (25 - k - 2):
            self.xps += self.vel


FLAG = Flag()
