'''This is manage.py '''
import os

class Manage():
    '''main class to manage scores, lives'''
    score = 0
    lives = 10
    time = 500
    coins = 0
    kill = 0
    bossLives = 5
    # Function to printthe Header (score, time, lives)
    @classmethod
    def printhead(cls):
        '''prints the header'''
        print("")
        print("TIME LEFT : " + str(Manage.time))
        print("YOUR SCORE IS : " +
              str(Manage.score) +
              "\t ENEMIES KILLED: " +
              str(Manage.kill) +
              "\t COINS:" +
              str(Manage.coins) +
              "\t     LIVES LEFT : " +
              str(Manage.lives))
        print("BOSS Lives: " + str(Manage.bossLives))
        print("")

    @classmethod
    def printbottom(cls):
        '''prints the bottom'''
        print("")
        print("YOU WIN")
        print("YOUR SCORE IS : " +
              str(Manage.score) +
              "\t ENEMIES KILLED: " +
              str(Manage.kill) +
              "\t COINS:" +
              str(Manage.coins) +
              "\t     LIVES LEFT : " +
              str(Manage.lives))
        print("")
    # Function to alter score

    @classmethod
    def changescore(cls, deleted):
        '''changes the score'''

        if deleted == 'coin':
            Manage.score += 10

        if deleted == 'brick':
            Manage.score += 50

        if deleted == 'enemy1':
            Manage.score += 100

        if deleted == 'enemy2':
            Manage.score += 200

        if deleted == 'boss':
            Manage.score += 1000

    # Function to alter lives
    @classmethod
    def changelives(cls):
        '''changes lives'''
        if Manage.lives == 1:
            os.system('pkill -kill aplay')
            os.system('aplay -q ./smb_gameover.wav&')
            print('GAME OVER')
            print('Your Final Score is : ' + str(Manage.score))
            print('')
            quit()
        else:
            Manage.lives -= 1

    # function for boss life
    @classmethod
    def bosslife(cls):
        '''change boss life'''
        if Manage.bossLives == 0:
            Manage.changescore('boss')
            Manage.bossLives = 'Defeated'
        elif Manage.bossLives != 'Defeated':
            Manage.bossLives -= 1

    @classmethod
    def coinscollect(cls):
        '''collect coins'''
        Manage.coins += 1
    # timer for functionality

    @classmethod
    def enemykill(cls):
        '''kill enemy'''
        Manage.kill += 1

    @classmethod
    def timer(cls):
        '''maintains timer'''
        if Manage.time == 0:
            print("Sorry, you ran out of time.")
            print("GAME OVER")
            print('Your Final Score is : ' + str(Manage.score))
            os.system('pkill -kill aplay')
            quit()
        else:
            Manage.time -= 1
