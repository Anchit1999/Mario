'''board.py'''
from config import FLOOR, PIPE, MOUNTAIN, WATER, BRICK, SURFACE


class Board():
    '''code for board of mario'''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.mat = []
        for i in range(self.height):
            self.mat.append([])

        for i in range(self.height):
            for j in range(self.width):
                self.mat[i+j-j].append(' ')

    def board_initialise(self, length):
        '''Initialise the board'''
        for i in range(30):
            for j in range(length, length + 80):
                self.mat[i][j] = ' '
        # earth_bricks
        for i in range(0, self.width, 1):
            self.mat[self.height - 2][i] = FLOOR
            self.mat[self.height - 3][i] = FLOOR
            self.mat[self.height - 4][i] = FLOOR

        # castle
        self.mat[25][520] = '|'
        self.mat[24][520] = '|'
        self.mat[23][520] = '|'
        self.mat[22][520] = '|'
        self.mat[25][538] = '|'
        self.mat[24][538] = '|'
        self.mat[23][538] = '|'
        self.mat[22][538] = '|'

        for i in range(522, 538, 2):
            self.mat[22][i] = '|'
        for i in range(521, 538, 2):
            if i % 4 == 1:
                self.mat[21][i] = '_'
            else:
                self.mat[22][i] = '_'

        self.mat[20][525] = '|'
        self.mat[19][525] = '|'
        self.mat[18][525] = '|'
        self.mat[20][533] = '|'
        self.mat[19][533] = '|'
        self.mat[18][533] = '|'

        self.mat[17][526] = '_'
        self.mat[17][527] = '_'
        self.mat[18][528] = '|'
        self.mat[18][530] = '|'
        self.mat[18][529] = '_'
        self.mat[17][531] = '_'
        self.mat[17][532] = '_'

        self.mat[25][528] = '*'
        self.mat[24][528] = '*'
        self.mat[24][529] = '*'
        self.mat[24][530] = '*'
        self.mat[25][531] = '*'
        self.mat[24][531] = '*'

    def make_pipe(self, i, hgt1):
        '''Make pipe'''
        for j in range(self.height - 4 - hgt1, self.height - 4):
            self.mat[j][i] = PIPE
            self.mat[j][i + 4] = PIPE

        for j in range(i, i + 5):
            self.mat[self.height - 4 - hgt1][j] = PIPE

        # spring
    def make_spring(self, i, j):
        '''Make Spring'''
        self.mat[j][i] = '/'
        self.mat[j - 1][i + 1] = '/'
        self.mat[j][i + 1] = '\\'
        self.mat[j - 1][i] = '\\'
        self.mat[j - 2][i] = '-'
        self.mat[j - 2][i + 1] = '-'

    def make_cloud(self, j, k):
        '''Make Cloud'''
        for i in range(0, self.width - 100, 90):
            self.mat[j][k + i] = '\033[1;36m(\033[1;m'
            self.mat[j][k + 1 + i] = '\033[1;36m_\033[1;m'
            self.mat[j][k + 2 + i] = '\033[1;36m_\033[1;m'
            self.mat[j][k + 3 + i] = '\033[1;36m_\033[1;m'
            self.mat[j][k + 4 + i] = '\033[1;36m)\033[1;m'
            self.mat[j - 1][k + 2 + i] = '\033[1;36m(\033[1;m'
            self.mat[j - 2][k + 3 + i] = '\033[1;36m_\033[1;m'
            self.mat[j - 2][k + 4 + i] = '\033[1;36m_\033[1;m'
            self.mat[j - 1][k + 5 + i] = '\033[1;36m)\033[1;m'
            self.mat[j][k + 5 + i] = '\033[1;36m_\033[1;m'
            self.mat[j][k + 6 + i] = '\033[1;36m_\033[1;m'
            self.mat[j][k + 7 + i] = '\033[1;36m)\033[1;m'

    def make_mountain(self, hgt2, mid):
        '''Make cloud'''
        for k in range(0, self.width - 100, 90):
            for i in range(self.height - 4 - hgt2, self.height - 4):
                for j in range(0, i - (self.height - 4 - hgt2)):
                    self.mat[i][k + mid - j] = MOUNTAIN
                    self.mat[i][k + mid + j] = MOUNTAIN

    def make_brick(self, i, j, sym, size):
        '''Make brick'''
        for xps in range(i, i + size):
            for yps in range(j, j + size):
                self.mat[xps][yps] = BRICK
        if size % 2 == 1 and sym != '*':
            self.mat[i + size // 2][j + size // 2] = sym

    def make_coin(self, i, j):
        '''Make coin'''
        self.mat[i][j] = '\x1b[1;35mO\x1b[1;m'

    def make_pit(self, j, size):
        '''Make pit'''
        for i in range(self.height - 4, self.height - 1):
            for k in range(j, j + size):
                if i == self.height - 4:
                    self.mat[i][k] = " "
                else:
                    self.mat[i][k] = WATER

    def checkstar(self, xps, yps):
        '''Check for asteric(*)'''
        if self.mat[xps][yps] == WATER:
            return 2
        for i in SURFACE:
            if self.mat[xps][yps] == i:
                return 1
        return 3
    # changing name of print

    def print_on_board(self, left, right):
        '''Print Board'''
        for i in range(self.height):
            for j in range(left, right):
                print(self.mat[i][j], end='')
            print('')


BOARD = Board(30, 620)
