import sys
sys.path.append('../')
from person import *
from board import *


def test_moveup():

	# print(PERSON.xpos,PERSON.ypos)
	Board.board_initialise(BOARD,0)
	PERSON = Person(25, 3, 8, 'm')
	prev_X = PERSON.xpos
	Person.moveup(PERSON)
	# print(PERSON.xpos,PERSON.ypos)
	assert PERSON.xpos < prev_X

def test_movedown():

	# print(PERSON.xpos,PERSON.ypos)
	Board.board_initialise(BOARD,0)
	PERSON = Person(25, 3, 8, 'm')
	Person.moveup(PERSON)
	# print(PERSON.xpos,PERSON.ypos)
	# print(PERSON.jump)
	i=0
	check = PERSON.xpos
	# print(check)
	while i < PERSON.jump:
		Person.movedown(PERSON,'w')
		i += 1
		check = PERSON.xpos
		# print(check)
		# print(PERSON.xpos,PERSON.ypos)
	assert check == 25
# test_movedown()

def test_moveright():

	Board.board_initialise(BOARD,0)
	PERSON = Person(25, 3, 8, 'm')
	prev_Y = PERSON.ypos
	Person.moveright(PERSON)

	assert PERSON.ypos == prev_Y+1

def test_moveleft():

	Board.board_initialise(BOARD,0)
	PERSON = Person(25, 3, 8, 'm')
	prev_Y = PERSON.ypos
	Person.moveleft(PERSON,0)

	assert PERSON.ypos == prev_Y-1