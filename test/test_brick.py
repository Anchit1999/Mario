import sys
sys.path.append('../')
from person import *
from board import *
from scene import Scene
from manage import Manage
from bricks import BRICK_LIST

def test_brickcollision1():
	'''Collision while coming down with the brick'''
	Scene.make_cm(0)
	PERSON.xpos = 25
	PERSON.ypos = 34
	PERSON.jump = 8
	Scene.brick_coin()
	Person.moveup(PERSON)

	for i in range(PERSON.jump-1):
		Person.movedown(PERSON,'w')

	# Board.board_initialise(BOARD,0)
	Scene.make_cm(0)
	Scene.brick_coin()
	Person.print_on_board(PERSON,PERSON.xpos,PERSON.ypos)
	Board.print_on_board(BOARD,0,80)
	# print(Manage.score)
	s1 = Manage.score
	Person.moveright(PERSON)
	Scene.brick_coin()
	# Board.board_initialise(BOARD,0)
	Scene.make_cm(0)
	Scene.brick_coin()
	s2 = Manage.score
	Person.print_on_board(PERSON,PERSON.xpos,PERSON.ypos)
	Board.print_on_board(BOARD,0,80)
	assert s1 == s2

# test_brickcollision1()

def test_brickcollision2():
	'''collision when 1 unit ahead of brick'''
	Scene.make_cm(0)
	PERSON.xpos = 25
	PERSON.ypos = 38
	PERSON.jump = 8
	Scene.brick_coin()

	Person.moveup(PERSON)
	# print(PERSON.xpos,PERSON.ypos)
	s1 = Manage.score
	prev_x = PERSON.xpos
	Person.movedown(PERSON,'w')
	while prev_x != PERSON.xpos:
		prev_x = PERSON.xpos
		Scene.brick_coin()
		Person.movedown(PERSON,'w')
	s2 = Manage.score
	# print(s1,s2)
	assert s2 > s1

# test_brickcollision2()

def test_score_brick():
	'''collecting coin when collision with brick'''
	# Board.board_initialise(BOARD,0)
	Scene.make_cm(0)
	PERSON.xpos = 25
	PERSON.ypos = 3
	PERSON.jump = 8
	for i in range(41):
		Person.moveright(PERSON)

	print(PERSON.xpos,PERSON.ypos)
	Scene.brick_coin()
	initial_bricks = len(BRICK_LIST)
	Person.moveup(PERSON)
	for i in range(PERSON.jump):
		Scene.brick_coin()
		Person.movedown(PERSON,'w')
	
	Person.moveup(PERSON)
	for i in range(PERSON.jump):
		Scene.brick_coin()
		Person.movedown(PERSON,'w')

	# print(Manage.score)
	# Board.board_initialise(BOARD,0)
	Scene.make_cm(0)
	Scene.brick_coin()
	final_bricks = len(BRICK_LIST)
	assert Manage.score > 0 and final_bricks == initial_bricks - 1

# test_score_brick()