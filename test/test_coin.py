import sys
sys.path.append('../')

from person import *
from board import *
from scene import Scene
from manage import Manage

def test_coin1():
	'''collect coin from right'''
	Scene.make_cm(0)
	Scene.make_pps()
	Scene.brick_coin()

	for i in range(61):
		Person.moveright(PERSON)

	Person.moveup(PERSON)
	Person.moveright(PERSON)

	prev_x = PERSON.xpos
	Person.movedown(PERSON,'w')
	while prev_x != PERSON.xpos:
		prev_x = PERSON.xpos
		Person.movedown(PERSON,'w')
	# print(PERSON.xpos,PERSON.ypos)
	Person.moveright(PERSON)
	Scene.brick_coin()
	# print(Manage.score)

	assert Manage.score > 0

# test_coin1()

def test_coin2():
	'''collect coin from left'''
	Scene.make_cm(0)
	PERSON.xpos = 25
	PERSON.ypos = 3
	PERSON.jump = 8
	Scene.make_pps()
	Scene.brick_coin()

	for i in range(61):
		Person.moveright(PERSON)

	Person.moveup(PERSON)
	Person.moveright(PERSON)

	prev_x = PERSON.xpos
	Person.movedown(PERSON,'w')
	while prev_x != PERSON.xpos:
		prev_x = PERSON.xpos
		Person.movedown(PERSON,'w')

	Person.moveup(PERSON)
	for _ in range(5):
		Person.moveright(PERSON)

	prev_x = PERSON.xpos
	Person.movedown(PERSON,'w')
	while prev_x != PERSON.xpos:
		prev_x = PERSON.xpos
		Person.movedown(PERSON,'w')
	
	Person.moveleft(PERSON,0)
	# print(PERSON.xpos,PERSON.ypos)
	# print(Manage.score)
	s1 = Manage.score
	Scene.brick_coin()
	# print(Manage.score)
	s2 = Manage.score
	assert s2 > s1

# test_coin2()

def test_coin3():
	'''collect coin while jumping'''

	Scene.make_cm(80)
	PERSON.xpos = 25
	PERSON.ypos = 151
	Scene.brick_coin()
	# print(Manage.score)
	s1 = Manage.score
	Person.moveup(PERSON)
	Scene.brick_coin()
	# print(Manage.score)
	s2 = Manage.score
	assert s2 > s1

# test_coin3()

def test_coin4():
	'''collect 2 coins at a time'''
	Scene.make_cm(80)
	PERSON.xpos = 25
	PERSON.ypos = 153
	Scene.brick_coin()
	# print(Manage.score)
	s1 = Manage.score
	Person.moveup(PERSON)
	Scene.brick_coin()
	# print(Manage.score)
	s2 = Manage.score
	assert s2 - s1 == 20

# test_coin4()