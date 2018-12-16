MARIO
==============
*Coded by:*
**Anchit Gupta**

This file contains :
 1. Rules of the Game
 2. Description of Classes Created
 3. Instructions on how to Run the Code
 4. Requirements

 ----------

Rules of the Game
------------

> - You control the Mario and you have to reach the castle in order to win the game
> - You will encounter multiple enemies on your way. Defeat and dodge the enemies to reach the end of the game and finally encounter boss enemy. 
> - You have 10 lives for Mario. You will lose a life if you get in *contact* with any enemy, *fall* in pit, or got *hit by enemy bullet*.
> - You have to climb on a *flagpost* after killing the boss, the higher you jump on it more points you will get.
> - You have 500 seconds to explore and win the game.

----------------------

Scoring
------------

>- 10 points for collecting coins.
>- 50 points for breaking brick.
>- 100 or 200 points on killing enemy depending on the type of enemy.
>- 1000 points on killing boss enemy.
>- Higher the jump on *flagpost* higher the points you get.

------------------

Description of Classes Created
--------------------------------
#### Board:
The board class contains 30 x 620 board out of which 80 are displayed at once. It contains functions like make_pipe,make_brick,make_coin,make_cloud,make_mountain and board initialise and Print functions.

#### Bricks:
This contains the function which creates the bricks which contain coins as well as unbreakable. It also contains the list of bricks.

#### Enemy:
This cointains the enemy move,collision,print functioins.

#### Manage:
Manage class manages printing scoreboard,killing enemies and mario and boss.

#### Person:
This class contains all the logic behind mario,movements,collision,landing on surface.

#### Boss:
This class contain Boss move,print functioins.

#### Coin,Bar,Bullet:
Contains the respective logics.

#### Scene:
This creates the scenery of the game.

#### P:
Used for polymorphism

------------------------

Features
--------------------------
> - There are two types of enemies. Normal enemy and Turtle enemy.
> - Jumping on normal enemy kills it instantly,but on jumping on turtle enemy it stops for once, we can *kick* it once it is stopped, if nothing is done to it, it will start travelling again. It can be killed by double jump.
> - As games progresses enemies start chasing Mario.
> - Game has checkpoints to respawn mario after getting out.
> - You can jump on the springs in case normal jump wont serve the purpose.
> - Game has a *bar* on which mario can stand and cross a *long* pit.
> - Have background sound.
> - There are different colors for different objects, bricks-brown,floor-grey,clouds-cyan,mountains-red,bar-magenta,water-blue.
> - A hidden power-up which enables mario to kill the boss enemy.
> - Game has a **cheat-code**. If you  are unable to find hidden power up you can always press p to enable bullets.
> - Boss Enemy randomly changing its position and firing bullets. 
> - Jump on flagpost at the end.
> - *Post Credit* Scene - Mario Reaching Castle.

How To Play:
------------------------
> - Run the following code to start the game.
```
python3 run.py
```
> - Press enter to start the game.
> - 'w, a, s, d' use these controls for up, left, down, and right.
> - use 'x' to fire a bullet after getting powerup(*hidden powerup*).
> - press 'q' to quit.
----------------------------

Reqirements:
--------------------
- Python3
- aplay for linux
- afplay for mac
For mac:
```
brew cask update
sudo brew cask install python3
```
For Linux:
```
sudo apt-get update
sudo apt-get install python3
```
