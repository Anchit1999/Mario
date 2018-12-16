'''This is boss.py'''
from board import BOARD


class Boss():
    '''Create boss'''
    bosstime = 0
    x = 25
    y = 460
    Health = 5

    @classmethod
    def print_on_board(cls, xps, yps):
        '''print boss'''
        BOARD.mat[xps][yps] = '\\'
        BOARD.mat[xps][yps + 1] = '/'
        BOARD.mat[xps - 1][yps + 2] = '_'
        BOARD.mat[xps][yps + 3] = '\\'
        BOARD.mat[xps][yps + 4] = '/'

        BOARD.mat[xps - 1][yps] = '|'
        BOARD.mat[xps - 2][yps] = '|'
        BOARD.mat[xps - 3][yps] = '|'
        BOARD.mat[xps - 1][yps + 4] = '|'
        BOARD.mat[xps - 2][yps + 4] = '|'
        BOARD.mat[xps - 3][yps + 4] = '|'

        BOARD.mat[xps - 2][yps + 1] = '^'
        BOARD.mat[xps - 2][yps + 2] = '^'
        BOARD.mat[xps - 2][yps + 3] = '^'

        BOARD.mat[xps - 3][yps + 1] = 'o'
        BOARD.mat[xps - 3][yps + 3] = 'o'

        BOARD.mat[xps - 4][yps + 1] = '_'
        BOARD.mat[xps - 4][yps + 2] = '_'
        BOARD.mat[xps - 4][yps + 3] = '_'
    def pos(self):
        '''return position'''
        pass


BOSS = Boss()
