'''This is code for bricks part'''
from board import BOARD


class Brick():
    '''brick'''
    def __init__(self, x, y, coin, sz):
        self.xps = x
        self.yps = y
        self.coin = coin
        self.size = sz

    def print_on_board(self, xps, yps):
        '''To print bricks'''
        BOARD.make_brick(xps, yps, self.coin, self.size)
    def score(self):
        '''score of a brick'''
        pass


BRICK_LIST = []
BRICK_LIST.append(Brick(20, 25, '*', 3))
BRICK_LIST.append(Brick(20, 35, 1, 3))
BRICK_LIST.append(Brick(20, 39, '*', 3))
BRICK_LIST.append(Brick(14, 43, '*', 3))
BRICK_LIST.append(Brick(20, 43, 2, 3))
BRICK_LIST.append(Brick(20, 47, '*', 3))
BRICK_LIST.append(Brick(20, 51, 3, 3))

BRICK_LIST.append(Brick(20, 175, 1, 3))
BRICK_LIST.append(Brick(20, 179, '*', 3))
BRICK_LIST.append(Brick(20, 183, 2, 3))
BRICK_LIST.append(Brick(14, 183, '*', 3))
BRICK_LIST.append(Brick(14, 186, '*', 3))
BRICK_LIST.append(Brick(14, 189, '*', 3))

for i in range(191, 213, 3):
    BRICK_LIST.append(Brick(8, i, '*', 3))

BRICK_LIST.append(Brick(20, 206, 5, 3))
BRICK_LIST.append(Brick(20, 222, 5, 3))
BRICK_LIST.append(Brick(20, 238, 5, 3))

BRICK_LIST.append(Brick(8, 220, '*', 3))
BRICK_LIST.append(Brick(8, 223, '*', 3))
BRICK_LIST.append(Brick(8, 226, '*', 3))
BRICK_LIST.append(Brick(8, 229, '*', 3))


for i in range(24, 17, -2):
    for j in range(356, 349 + 24 - i, -2):
        BRICK_LIST.append(Brick(i, j, '*', 2))

for i in range(24, 17, -2):
    for j in range(362, 369 - 24 + i, 2):
        BRICK_LIST.append(Brick(i, j, '*', 2))

for i in range(24, 17, -2):
    for j in range(397, 388 + 24 - i, -2):
        BRICK_LIST.append(Brick(i, j, '*', 2))

for i in range(24, 9, -2):
    for j in range(486, 471 + 24 - i, -2):
        BRICK_LIST.append(Brick(i, j, '*', 2))
