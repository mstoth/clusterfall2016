from Maze import *
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

    def testScreenExists(self):
        assert type(self.m.s) == turtle._Screen
        assert self.m.s.window_width == self.m.size
        assert self.m.s.bgcolor() == 'blue'

    def testTurtleExists(self):
        assert type(self.m.t) == turtle.Turtle

    def testForMatrix(self):
        assert len(self.m.matrix)==SIZE/20

    def testReset(self):
        self.m.reset()
        assert self.m.matrix[0][0]==0
        assert self.m.t.pos()==(-(SIZE/2-10),SIZE/2-10)

    def testGetMatrixValueAt(self):
        self.m.reset()
        xpos = -(self.m.size/2-10)
        ypos = self.m.size/2-10
        assert self.m.getMatrixValueAt((xpos,ypos))==0 

    def testDirection(self):
        self.m.reset()
        self.m.t.goto(0,0)
        assert self.m.direction((0,0),(10,0))==EAST
        assert self.m.direction((0,0),(-10,0))==WEST
        assert self.m.direction((0,0),(0,10))==NORTH
        assert self.m.direction((0,0),(0,-10))==SOUTH

    def testSetMatrixValueAt(self):
        self.m.reset()
        self.m.setMatrixValueAt((0,0),-1)
        assert self.m.getMatrixValueAt((0,0))==-1

    def testTooClose(self):
        self.m.reset()
        assert self.m.tooClose(NORTH)==True
        assert self.m.tooClose(EAST)==False
        assert self.m.tooClose(SOUTH)==False
        assert self.m.tooClose(WEST)==True
        


if __name__=='__main__':
    unittest.main()
