from Maze3 import *
import random
import turtle
import unittest

SIZE = 420

class testMaze3(unittest.TestCase):

    EAST=2
    SOUTH=1
    WEST=3
    NORTH=0

    def setUp(self):
        # this checks for a Maze class
        self.m=Maze3(SIZE)

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

##    def testTooClose(self):
##        self.m.reset()
##        assert self.m.tooClose(NORTH)==True
##        assert self.m.tooClose(EAST)==False
##        assert self.m.tooClose(SOUTH)==False
##        assert self.m.tooClose(WEST)==True

##    def testDig(self):
##        self.m.reset()
##        spos = self.m.t.pos()
##        self.m.dig(EAST)
##        assert self.m.t.pos()==(spos[0]+self.m.pathWidth,spos[1])
##        spos=self.m.t.pos()
##        self.m.dig(SOUTH)
##        assert self.m.t.pos()==(spos[0],spos[1]-self.m.pathWidth)
##        spos=self.m.t.pos()
##        self.m.dig(WEST)
##        assert self.m.t.pos()==(spos[0],spos[1])
##        self.m.t.goto(0,0)
##        self.m.dig(NORTH)
##        assert self.m.t.pos()==(0,self.m.pathWidth)

##        # make sure we can't dig west from a reset
##        self.m.reset()
##        spos = self.m.t.pos()
##        self.m.dig(WEST)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig north from a reset
##        self.m.reset()
##        self.m.dig(NORTH)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig east from the right hand corner
##        self.m.reset()
##        self.m.t.goto(self.m.size/2-self.m.pathWidth/2,self.m.size/2-self.m.pathWidth/2)
##        spos=self.m.t.pos()
##        self.m.dig(EAST)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig south from the lower right hand corner
##        self.m.reset()
##        self.m.t.goto((self.m.size/2-self.m.pathWidth/2,-(self.m.size/2-self.m.pathWidth/2)))
##        spos=self.m.t.pos()
##        self.m.dig(SOUTH)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig east
##        # if it would break through to an existing space
##        self.m.reset()
##        self.m.setMatrixValueAt((-(self.m.size/2-5*self.m.pathWidth/2),self.m.size/2-self.m.pathWidth/2),0)
##        spos=self.m.t.pos()
##        self.m.dig(EAST)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig south
##        # if it would break through to an existing space
##        self.m.reset()
##        self.m.setMatrixValueAt((-(self.m.size/2-self.m.pathWidth/2),self.m.size/2-5*self.m.pathWidth/2),0)
##        spos=self.m.t.pos()
##        self.m.dig(SOUTH)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig west
##        # if it would break through to an existing space
##        self.m.reset()
##        self.m.setMatrixValueAt((-(self.m.size/2-5*self.m.pathWidth/2),self.m.size/2-self.m.pathWidth/2),0)
##        self.m.t.goto(-(self.m.size/2-5*self.m.pathWidth/2),self.m.size/2-self.m.pathWidth/2)
##        spos=self.m.t.pos()
##        self.m.dig(WEST)
##        assert self.m.t.pos()==spos
##        # make sure we can't dig north
##        # if it would break through to an existing space
##        self.m.reset()
##        self.m.setMatrixValueAt((-(self.m.size/2-self.m.pathWidth/2),self.m.size/2-5*self.m.pathWidth/2),0)
##        self.m.t.goto(-(self.m.size/2-self.m.pathWidth/2),self.m.size/2-5*self.m.pathWidth/2)
##        spos=self.m.t.pos()
##        self.m.dig(NORTH)
##        assert self.m.t.pos()==spos

##    def testReturnValuesOfDig(self):
##        self.m.reset()
##        self.m.t.goto((-110,110))
##        assert self.m.dig(EAST)==(-90,110)
##        self.m.reset()
##        self.m.t.goto((-110,110))
##        assert self.m.dig(SOUTH)==(-110,90)
##        self.m.reset()
##        self.m.t.goto((-110,110))
##        assert self.m.dig(NORTH)==(-110,130)
##        self.m.reset()
##        self.m.t.goto((-110,110))
##        assert self.m.dig(WEST)==(-130,110)
        
##    def testDigRefusesIfCornersAreEmpty(self):
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((2*self.m.pathWidth,self.m.pathWidth),0)
##        self.m.dig(EAST)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((2*self.m.pathWidth,-self.m.pathWidth),0)
##        self.m.dig(EAST)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((self.m.pathWidth,-2*self.m.pathWidth),0)
##        self.m.dig(SOUTH)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((-self.m.pathWidth,-2*self.m.pathWidth),0)
##        self.m.dig(SOUTH)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((-2*self.m.pathWidth,self.m.pathWidth),0)
##        self.m.dig(WEST)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((-2*self.m.pathWidth,-self.m.pathWidth),0)
##        self.m.dig(WEST)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((self.m.pathWidth,2*self.m.pathWidth),0)
##        self.m.dig(NORTH)
##        assert self.m.t.pos()==(0,0)
##        self.m.reset()
##        self.m.t.goto(0,0)
##        self.m.setMatrixValueAt((-self.m.pathWidth,2*self.m.pathWidth),0)
##        self.m.dig(NORTH)
##        assert self.m.t.pos()==(0,0)

##    def testNeighbors(self):
##        self.m.reset()
##        va=[]
##        n=self.m.neighbors()
##        for nn in n:
##            va.append(nn[1])
##        assert va == [-1,1,1,-1]

##    def testBackToWall(self):
##        self.m.reset()
##        spos = self.m.t.pos()
##        self.m.dig(EAST)
##        self.m.dig(EAST)
##        self.m.dig(SOUTH)
##        self.m.dig(SOUTH)
##        self.m.dig(WEST)
##        self.m.dig(WEST)
##        assert self.m.t.pos() == (spos[0],spos[1]-2*self.m.pathWidth)

if __name__=='__main__':
    unittest.main()
