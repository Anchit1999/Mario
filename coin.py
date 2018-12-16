'''coin.py'''
from board import BOARD

class Coin():
    '''code for coins in the game'''
    def __init__(self, xps, yps):
        self.xps = xps
        self.yps = yps
    @classmethod
    def print_on_board(cls, xps, yps):
        '''print the coins'''
        BOARD.make_coin(xps, yps)
    def score(self):
        '''score'''
        pass


COIN_LIST = []
COIN_LIST.append(Coin(21, 66))
COIN_LIST.append(Coin(21, 68))
COIN_LIST.append(Coin(21, 150))
COIN_LIST.append(Coin(21, 151))
COIN_LIST.append(Coin(21, 152))
COIN_LIST.append(Coin(21, 153))
COIN_LIST.append(Coin(21, 250))
COIN_LIST.append(Coin(22, 260))
COIN_LIST.append(Coin(20, 265))
COIN_LIST.append(Coin(21, 271))
COIN_LIST.append(Coin(22, 279))
COIN_LIST.append(Coin(23, 351))
COIN_LIST.append(Coin(21, 353))
COIN_LIST.append(Coin(19, 355))
COIN_LIST.append(Coin(17, 357))
COIN_LIST.append(Coin(21, 375))
COIN_LIST.append(Coin(21, 377))
COIN_LIST.append(Coin(21, 379))
COIN_LIST.append(Coin(21, 381))
