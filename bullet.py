'''This is bullet.py'''
class Bullet():
    '''Bullet info'''
    def __init__(self, x, y, v, s):
        self.xps = x
        self.yps = y
        self.vel = v
        self.sym = s
        self.tym = 0
    def position(self):
        '''return position of bullet'''
        return (self.xps, self.yps)
    def spawntime(self):
        '''return spawntime of bullet'''
        return self.tym


# bullet_list = []
# boss_bullet = []
BULLET_LIST = []
BOSS_BULLET = []
