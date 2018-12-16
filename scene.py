'''This is scene.py '''
import os
import time
import random
from board import BOARD
from enemy import ELIST
from bricks import BRICK_LIST, Brick
from person import CHECKPOINT, PERSON
from manage import Manage
from config import BOSS_B
from polymorph import POLY
from move_bar import BLIST
from flag import FLAG
from coin import COIN_LIST
from boss import BOSS
from bullet import BULLET_LIST, BOSS_BULLET, Bullet


class Scene():
    '''code for creating scene'''
    # make cloud mountain

    @classmethod
    def make_cm(cls, k):
        '''make cloud and mountain'''
        BOARD.board_initialise(k)  # board initialisation
        BOARD.make_cloud(6, 25)
        BOARD.make_cloud(4, 45)
        BOARD.make_mountain(8, 10)
        BOARD.make_mountain(4, 50)

    # for brick and coins
    @classmethod
    def brick_coin(cls):
        '''make brick, coin'''
        flag = 0
        for k in BRICK_LIST:
            POLY.print_poly(k, k.xps, k.yps)
            if PERSON.xpos == 18 and PERSON.ypos >= 345 and PERSON.ypos <= 347 and flag == 0:
                PERSON.sym = 'M'
                try:
                    sound = open('smb_powerup.wav', 'r')
                    os.system('aplay -q ./smb_powerup.wav&')
                except:
                    pass
                BRICK_LIST.append(Brick(14, 345, '*', 3))
                flag = 1

            # print(PERSON.xpos,PERSON.ypos,k.xps,k.yps)
            if PERSON.xpos == k.xps + 4 and PERSON.ypos >= k.yps and PERSON.ypos <= k.yps + 2:
                if k.coin != '*' and k.coin != 0:
                    k.coin -= 1
                    try:
                        sound = open('smb_coin.wav', 'r')
                        os.system('aplay -q ./smb_coin.wav&')
                    except:
                        pass
                    Manage.coinscollect()
                    Manage.changescore('coin')
                else:
                    try:
                        sound = open('smb_bump.wav', 'r')
                        os.system('aplay -q ./smb_bump.wav&')
                    except:
                        pass
            if k.coin == 0:
                BRICK_LIST.remove(k)
                try:
                    sound = open('smb_breakblock.wav', 'r')
                    os.system('aplay -q ./smb_breakblock.wav&')
                except:
                    pass
                Manage.changescore('brick')

        for k in COIN_LIST:
            # k.print_coin(k.x,k.y)
            POLY.print_poly(k, k.xps, k.yps)
            if PERSON.xpos == k.xps and PERSON.ypos == k.yps:
                try:
                    sound = open('smb_coin.wav', 'r')
                    os.system('aplay -q ./smb_coin.wav&')
                except:
                    pass
                Manage.coinscollect()
                COIN_LIST.remove(k)
                Manage.changescore('coin')

    # moving bar
    @classmethod
    def moving_bar(cls):
        '''make moving bar'''
        for k in BLIST:
            if time.time() - k.tym > 0.2:
                k.tym = time.time()
                k.yps += k.vel
                if PERSON.ypos == k.yps - 1 and PERSON.xpos + 1 == k.xps and k.vel > 0:
                    PERSON.ypos = k.yps
                elif PERSON.ypos == k.yps + k.lgt and PERSON.xpos + 1 == k.xps and k.vel < 0:
                    PERSON.ypos = k.yps + k.lgt - 1
                elif k.xps == PERSON.xpos + 1 and PERSON.ypos >= k.yps \
                and PERSON.ypos < k.yps + k.lgt:
                    PERSON.ypos += k.vel

                # k.make_move()
                POLY.move_poly(k)
            k.make_bar(k.xps, k.yps, k.lgt)

    # PIPE,PITS AND SPRING
    @classmethod
    def make_pps(cls):
        '''make pipe, pit, spring'''
        BOARD.make_pipe(65, 4)
        BOARD.make_pipe(90, 5)
        BOARD.make_pipe(120, 6)
        BOARD.make_pipe(140, 4)
        BOARD.make_pit(160, 5)
        BOARD.make_spring(359, 25)
        BOARD.make_pit(200, 45)
        BOARD.make_pit(403, 10)
        BOARD.make_spring(400, 25)
        BOARD.make_pipe(430, 6)
        BOARD.make_spring(495, 18)

    @classmethod
    def make_flag(cls):
        '''make end flag'''
        # FLAG.print_FLAGag(FLAG.x)
        POLY.print_poly(FLAG, FLAG.xps)
        if PERSON.ypos == 504:
            if FLAG.first == 0:
                try:
                    sound = open('smb_flagpole.wav', 'r')
                    os.system('aplay -q ./smb_flagpole.wav&')
                except:
                    pass
                FLAG.first = PERSON.xpos - 1
            # print(FLAG.first)
            # FLAG.move(FLAG.first)
            POLY.move_poly(FLAG, FLAG.first)
            Manage.changescore('enemy1')

    @classmethod
    def enemy(cls, lgt):
        '''make enemy bullets'''
        # for bullets
        for k in BULLET_LIST:
            BOARD.mat[k.xps][k.yps] = k.sym
            if time.time() - k.tym > 0.1:
                k.tym = time.time()
                if BOARD.checkstar(k.xps, k.yps + 1) is 1 or k.yps > lgt + 80:
                    BULLET_LIST.remove(k)
                else:
                    k.yps += k.vel
            if k.xps >= 22 and k.xps <= 25 and k.yps == BOSS.y and BOSS.Health >= 0:
                Manage.bosslife()
                BULLET_LIST.remove(k)
                BOSS.Health -= 1

        if BOSS.Health >= 0:
            if time.time() - BOSS.bosstime > 1:
                BOSS.bosstime = time.time()
                BOSS.x = random.randint(22, 25)
                BOSS.y = random.randint(460, 470)
                BOSS_BULLET.append(Bullet(BOSS.x - 2, BOSS.y, -1, BOSS_B))
                prob = random.randint(1, 100)
                if prob < 20:
                    BOSS_BULLET.append(Bullet(BOSS.x - 3, BOSS.y, -1, BOSS_B))
                if prob < 10:
                    BOSS_BULLET.append(Bullet(BOSS.x - 1, BOSS.y, -1, BOSS_B))
                if prob == 2:
                    BOSS_BULLET.append(Bullet(BOSS.x, BOSS.y, -1, BOSS_B))

            if PERSON.xpos <= 25 and PERSON.xpos >= 22 and PERSON.ypos >= BOSS.y \
            and PERSON.ypos <= BOSS.y + 5:
                Manage.changelives()
                zps = 0
                for i, j in CHECKPOINT:
                    if j >= PERSON.ypos and i is not None:
                        PERSON.xpos = CHECKPOINT[zps - 1][0]
                        PERSON.ypos = CHECKPOINT[zps - 1][1]
                        break
                    zps += 1
            for k in BOSS_BULLET:
                if (k.xps >= PERSON.xpos -
                        1 and k.xps <= PERSON.xpos or k.xps +
                        1 == PERSON.xpos) and (k.yps >= PERSON.ypos -
                                               1 and k.yps <= PERSON.ypos):
                    Manage.changelives()
                    BOSS_BULLET.remove(k)
            for k in BOSS_BULLET:
                BOARD.mat[k.xps][k.yps] = k.sym
                if time.time() - k.tym > 0.1:
                    k.tym = time.time()
                    if BOARD.checkstar(k.xps, k.yps - 1) is 1 or k.yps < lgt:
                        BOSS_BULLET.remove(k)
                    else:
                        k.yps += k.vel
            # BOSS.print_boss(BOSS.x,BOSS.y)
            POLY.print_poly(BOSS, BOSS.x, BOSS.y)
        # print(lgt)
        for k in ELIST:
            if k.type == "enemy1":
                flagvar = False
                if time.time() - k.tym > 0.5:
                    k.tym = time.time()
                    if k.yps >= lgt and k.yps <= lgt + 80:
                        # k.move(None)
                        POLY.move_poly(k)
                if(PERSON.xpos == k.xps and PERSON.ypos == k.yps):
                    Manage.changelives()
                    flagvar = True
                    zps = 0
                    for i, j in CHECKPOINT:
                        if j >= PERSON.ypos:
                            PERSON.xpos = CHECKPOINT[zps - 1][0]
                            PERSON.ypos = CHECKPOINT[zps - 1][1]
                            break
                        zps += 1
                if PERSON.xpos + \
                        1 == k.xps and (PERSON.ypos - 1 == k.yps or PERSON.ypos == k.yps):
                    try:
                        sound = open('smb_stomp.wav', 'r')
                        os.system('aplay -q ./smb_stomp.wav&')
                    except:
                        pass
                    Manage.enemykill()
                    Manage.changescore(k.type)
                    PERSON.xpos -= 2
                    ELIST.remove(k)
                if lgt > 100:
                    if PERSON.xpos == k.xps:
                        if k.vel > 0 and PERSON.ypos < k.yps - 4:
                            k.vel = -k.vel
                        if k.vel < 0 and PERSON.ypos > k.yps + 4:
                            k.vel = -k.vel
                if k.xps == 26:
                    BOARD.mat[k.xps][k.yps] = ' '
                    ELIST.remove(k)
                # k.print_enemy(k.xps,k.yps)
                POLY.print_poly(k, k.xps, k.yps)

                if flagvar:
                    return PERSON.ypos - 10

            if k.type == "enemy2":  # TURTLE ENEMY
                flagvar = False
                if time.time() - k.tym > 5 and k.sym == ' ':
                    k.tym = time.time()
                    k.sym = '^'
                    k.vel = random.randrange(-1, 2, 2)
                    if k.yps >= lgt and k.yps <= lgt + 80:
                        # k.move()
                        POLY.move_poly(k)

                if PERSON.xpos == k.xps and PERSON.ypos + \
                        1 == k.yps and k.sym == ' ' and k.vel == 0:
                    try:
                        sound = open('smb_kick.wav', 'r')
                        os.system('aplay -q ./smb_kick.wav&')
                    except:
                        pass
                    k.vel = 1

                if PERSON.xpos == k.xps and PERSON.ypos - \
                        2 == k.yps and k.sym == ' ' and k.vel == 0:
                    try:
                        sound = open('smb_kick.wav', 'r')
                        os.system('aplay -q ./smb_kick.wav&')
                    except:
                        pass
                    k.vel = -1

                # enemy-enemy collision
                if k.sym == ' ' and k.vel != 0 and time.time() - k.tym > 0.1:
                    k.tym = time.time()
                    if k.yps >= lgt and k.yps <= lgt + 80:
                        POLY.move_poly(k)
                        for enmy in ELIST:
                            if(enmy.xps == k.xps and enmy.yps == k.yps and k != enmy):
                                try:
                                    sound = open('smb_stomp.wav', 'r')
                                    os.system('aplay -q ./smb_stomp.wav&')
                                except:
                                    pass
                                Manage.enemykill()
                                Manage.changescore(enmy.type)
                                ELIST.remove(enmy)

                if time.time() - k.tym > 0.5 and k.sym == '^':
                    k.tym = time.time()
                    if k.yps >= lgt and k.yps <= lgt + 80:
                        POLY.move_poly(k)

                if(PERSON.xpos == k.xps and (PERSON.ypos == k.yps or PERSON.ypos -
                                             1 == k.yps) and k.vel != 0):
                    Manage.changelives()
                    flagvar = True
                    zps = 0
                    for i, j in CHECKPOINT:
                        if j >= PERSON.ypos:
                            PERSON.xpos = CHECKPOINT[zps - 1][0]
                            PERSON.ypos = CHECKPOINT[zps - 1][1]
                            break
                        zps += 1

                if(PERSON.xpos + 2 == k.xps and (PERSON.ypos == k.yps or PERSON.ypos -
                                                 1 == k.yps) and k.sym == '^'):
                    k.sym = ' '
                    k.tym = time.time()
                    PERSON.xpos -= 2
                    k.vel = 0

                if(PERSON.xpos + 1 == k.xps and (PERSON.ypos == k.yps or PERSON.ypos -
                                                 1 == k.yps) and k.sym == ' '):
                    try:
                        sound = open('smb_stomp.wav', 'r')
                        os.system('aplay -q ./smb_stomp.wav&')
                    except:
                        pass
                    Manage.enemykill()
                    Manage.changescore(k.type)
                    PERSON.xpos -= 2
                    ELIST.remove(k)

                if lgt > 100:
                    if PERSON.xpos == k.xps and k.sym == '^':
                        if k.vel > 0 and PERSON.ypos < k.yps - 4:
                            k.vel = -k.vel
                        if k.vel < 0 and PERSON.ypos > k.yps + 4:
                            k.vel = -k.vel
                if k.xps == 26:
                    BOARD.mat[k.xps][k.yps] = ' '
                    ELIST.remove(k)

                # k.print_enemy(k.xps,k.yps,k.sym)
                POLY.print_poly(k, k.xps, k.yps)

                if flagvar:
                    return PERSON.ypos - 10
        return lgt
