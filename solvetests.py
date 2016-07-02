from Maze import *
import random
import turtle
import unittest

SIZE = 420

class testMaze(unittest.TestCase):

    EAST=2
    SOUTH=1
    WEST=3
    NORTH=0

    def setUp(self):
        # this checks for a Maze class
        self.m=Maze(SIZE)

    def testLeaveVisited(self):
        self.m.reset()
        [self.m.dig(EAST) for i in range(3)]
        self.m.t.goto(-self.m.size/2+self.m.pathWidth/2,self.m.size/2-self.m.pathWidth/2)
        [self.m.travel(EAST) for i in range(3)]
        assert self.m.matrix[1][0]==VISITED
        assert self.m.matrix[2][0]==VISITED
        assert self.m.t.pos()==(-self.m.size/2+7*self.m.pathWidth/2,self.m.size/2-self.m.pathWidth/2)
        [self.m.travel(WEST) for i in range(3)]
        assert self.m.matrix[2][0]==FAILED


if __name__=='__main__':
    unittest.main()
