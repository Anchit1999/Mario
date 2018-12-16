'''person.py'''
import os
import sys
import signal
from board import BOARD
from config import MARIO_B
from bullet import BULLET_LIST, Bullet
from getch import _getChUnix as getChar
from alarm_exception import AlarmException

CHECKPOINT = [
    [
        25, 2], [
            21, 66], [
                25, 115], [
                    25, 140], [
                        25, 155], [
                            25, 180], [
                                25, 250], [
                                    16, 396], [
                                        25, 450], [
                                            18, 430], [
                                                25, 550]]


class Person():
    '''code for mario'''
    def __init__(self, xpos, ypos, jump, sym):
        self.xpos = xpos
        self.ypos = ypos
        self.jump = jump
        self.sym = sym
        BOARD.mat[self.xpos][self.ypos] = sym

        # check any obstacle in jump
    def checkjump(self):
        '''jump of mario'''
        for i in range(self.xpos, self.xpos - self.jump, -1):
            if BOARD.checkstar(
                    i - 2,
                    self.ypos) is 1 or BOARD.checkstar(
                        i - 2,
                        self.ypos - 1) is 1:
                self.jump = self.xpos - i + 1
                break
    def moveup(self):
        '''move up'''
        oldxpos = self.xpos
        if BOARD.checkstar(
                oldxpos + 1,
                self.ypos) is 1 or BOARD.checkstar(
                    oldxpos + 1,
                    self.ypos - 1) is 1:
            self.checkjump()
            # print(self.jump)
            if BOARD.mat[self.xpos + 1][self.ypos] == '-':
                self.jump = 12
            self.xpos = self.xpos - self.jump
        return self.xpos

    def movedown(self, key):
        '''movedown'''
        # come down until there is no surface
        # if(BOARD.mat[self.xpos+1][self.ypos] != '*' and
        # BOARD.mat[self.xpos+1][self.ypos] != '-'):
        if BOARD.checkstar(
                self.xpos + 1,
                self.ypos) != 1 and BOARD.checkstar(
                    self.xpos + 1,
                    self.ypos - 1) != 1:
            self.xpos += 1
            if key == 'd' and BOARD.checkstar(self.xpos, self.ypos + 1) != 1:
                self.ypos += 1
            if key == 'a' and BOARD.checkstar(self.xpos, self.ypos - 2) != 1:
                self.ypos -= 1
    def moveright(self):
        '''moveright'''
        if BOARD.checkstar(self.xpos, self.ypos + 1) != 1:
            self.ypos += 1

    def moveleft(self, i):
        '''moveleft'''
        if BOARD.checkstar(self.xpos, self.ypos -
                           2) != 1 and self.ypos > i + 1:
            self.ypos -= 1

    def print_on_board(self, xps, yps):
        '''print mario on board'''
        BOARD.mat[xps - 1][yps] = self.sym
        BOARD.mat[xps - 1][yps - 1] = self.sym
        BOARD.mat[xps][yps] = '\\'
        BOARD.mat[xps][yps - 1] = '/'

    def move(self, i):
        '''move'''
        def alarmhandler(signum, frame):
            ''' input method '''
            if signum and frame:
                pass
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        key = user_input()
        self.jump = 8
        if key == 'q':
            os.system('pkill -kill aplay')
            sys.exit(0)
        # left
        if key == 'd':
            self.moveright()
        # right
        if key == 'a':
            self.moveleft(i)
        # up
        if key == 'w':
            self.moveup()
            # print(self.xpos)


            os.system('aplay -q ./smb_jump-small.wav&')
        # cheat-code
        if key == 'p':
            self.sym = 'M'
        # bullets
        if key == 'x' and self.sym == 'M':
            BULLET_LIST.append(Bullet(PERSON.xpos, PERSON.ypos + 1, 1, MARIO_B))

        self.movedown(key)

PERSON = Person(25, 3, 8, 'm')
