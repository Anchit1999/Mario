'''This is code for enemy'''
from board import BOARD

class Enemy():
    '''class enemy'''
    def __init__(self, xps, yps, vel, sym, no):
        self.xps = xps
        self.yps = yps
        self.vel = vel
        self.sym = sym
        self.type = no
        self.tym = 0

    def collision(self, xps, yps):
        '''code for collision'''
        if BOARD.checkstar(xps, yps + self.vel) == 1:
            self.vel = -self.vel

    def move(self, i=None):
        '''for enemy movement'''
        if BOARD.checkstar(self.xps + 1, self.yps) != 1 and i is None:
            self.xps += 1
            # BOARD.plr(pre_x,pre_y,self.x,self.y,self.sym)
        self.collision(self.xps, self.yps)
        self.yps += self.vel
        # BOARD.plr(self.x,pre_y,self.x,self.y,self.sym)
    def print_on_board(self, xps, yps):
        '''print enemy'''
        BOARD.mat[xps][yps] = self.sym


ELIST = []
ELIST.append(Enemy(18, 70, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 95, 1, '@', "enemy1"))
ELIST.append(Enemy(25, 126, 1, '@', "enemy1"))
ELIST.append(Enemy(25, 136, -1, '@', "enemy1"))
ELIST.append(Enemy(7, 200, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 260, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 265, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 310, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 315, -1, '@', "enemy1"))
ELIST.append(Enemy(25, 325, +1, '@', "enemy1"))
ELIST.append(Enemy(25, 330, +1, '@', "enemy1"))


class Enemy1(Enemy):
    '''Turle enemy'''
    # DUCK DUCK
    def print_on_board(self, xps, yps):
        '''print turtle enemy'''
        BOARD.mat[xps - 1][yps] = self.sym
        BOARD.mat[xps][yps] = 'D'


ELIST.append(Enemy1(25, 15, 1, '^', "enemy2"))
ELIST.append(Enemy1(25, 35, 1, '^', "enemy2"))
ELIST.append(Enemy1(25, 98, -1, '^', "enemy2"))
ELIST.append(Enemy1(25, 275, -1, '^', "enemy2"))
