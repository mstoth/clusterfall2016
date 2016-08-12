import turtle
import random
EMPTY=0

EAST=2
SOUTH=1
WEST=3
NORTH=0


EMPTY=0
WALL=1
GOAL=2
VISITED=3
FAILED=4
INVALID=-1


class Maze3():
    def __init__(self,size=440,pathWidth=20):
        self.size=size
        self.pathWidth=pathWidth
        self.reset()
