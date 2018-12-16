import sys
sys.path.append('../')
from person import *
from board import *
from scene import Scene
from manage import Manage

def test_enemy():

	Scene.make_cm(0)
	PERSON.xpos = 25
	PERSON.ypos = 15
	PERSON.jump = 8

	Scene.enemy(0)
	Person.moveup(PERSON)
	# print(Manage.score)
	Person.moveright(PERSON)
	prev_x = PERSON.xpos
	Person.movedown(PERSON,'w')
	while prev_x != PERSON.xpos:
		prev_x = PERSON.xpos
		Scene.enemy(0)
		Person.movedown(PERSON,'w')
	# print(Manage.score)
	# print(Manage.kill)
	# Person.print_on_board(PERSON,PERSON.xpos,PERSON.ypos)
	# Board.print_on_board(BOARD,0,80)
	assert Manage.score > 0 and Manage.kill > 0

# test_enemy()