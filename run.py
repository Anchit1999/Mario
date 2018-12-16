'''main mario file'''
import os
from polymorph import POLY
from board import BOARD
from scene import Scene
from person import PERSON, CHECKPOINT
from manage import Manage

SCENE = Scene()
M = Manage()
i = 0
MID = 0
TIMER = 0
os.system('aplay -q ./mario-theme.wav&')
while i <= BOARD.width - 80:
    if PERSON.xpos == 25 and PERSON.ypos == 504:
        break
    os.system("clear")
    M.printhead()
    SCENE.make_cm(i)
    SCENE.make_pps()
    SCENE.brick_coin()
    SCENE.moving_bar()
    SCENE.make_flag()
    i = SCENE.enemy(i)
    # PERSON.print_mario(PERSON.xpos,PERSON.ypos)
    POLY.print_poly(PERSON, PERSON.xpos, PERSON.ypos)
    # BOARD.print_board(i,i+80)
    POLY.print_poly(BOARD, i, i + 80)
    # PERSON.move(i)
    POLY.move_poly(PERSON, i)
    if BOARD.checkstar(PERSON.xpos + 1, PERSON.ypos) == 2:
        Manage.changelives()
        ZPS = 0
        for k, j in CHECKPOINT:
            if j >= PERSON.ypos:
                PERSON.xpos = CHECKPOINT[ZPS - 1][0]
                PERSON.ypos = CHECKPOINT[ZPS - 1][1]
                i = PERSON.ypos - 10
                break
            ZPS += 1
    if TIMER == 5:

        M.timer()
        TIMER = 0

    TIMER += 1

    MID = (i + i + 80) // 2
    if PERSON.ypos >= MID:
        i = i + 1

PERSON.xpos = 25
PERSON.ypos = 510

os.system('pkill -kill aplay')
os.system('aplay -q ./smb_stage_clear.wav&')
while PERSON.ypos != 530:
    os.system("sleep 0.1")
    os.system("clear")
    M.printhead()
    SCENE.make_cm(i)
    POLY.print_poly(PERSON, PERSON.xpos, PERSON.ypos)
    POLY.print_poly(BOARD, i, i + 80)
    i += 1
    PERSON.ypos += 1

Manage.printbottom()
