'''To have polymorphism in code'''
class Poly:
    '''Polymorphism code'''
    @classmethod
    def move_poly(cls, to_move, i=None):
        '''move polymorphism'''
        to_move.move(i)
    @classmethod
    def print_poly(cls, to_print, xps, yps=None):
        '''print polymorphism'''
        to_print.print_on_board(xps, yps)

POLY = Poly()
