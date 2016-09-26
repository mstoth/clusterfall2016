import random
import turtle
import unittest
from Maze import *

class testMaze(unittest.TestCase):
    """
    This class inherits from a class called TestCase which is
    defined in the unittest module.

    When you inherit from a class, you get all the methods that are
    defined in that class for free.

    Since this is a TestCase class, calling unittest.main() will automatically
    run any of the functions that start with the word 'test'
    """
    
    def setUp(self):
        """
        The setUp function is called each time one of your tests is run.
        We create an instance of the maze here before each test.
        """
        self.m=Maze()
        self.m.reset()

    def testMazeExists(self):
        """
        this will check to see if we have a maze class but as soon
        as setUp is run, we will see a failure so we really don't need
        to do anything here
        """
        pass
    
    def testScreenExists(self):
        assert type(self.m.s) == turtle._Screen

    def testTurtleExists(self):
        assert type(self.m.t) == turtle.Turtle

    def testScreenBackgroundIsBlue(self):
        assert self.m.s.bgcolor()=='blue'

    def testForMatrix(self):
        assert len(self.m.matrix)==20

    def testTurtleIsWhite(self):
        assert self.m.t.color()[0]=='white' and self.m.t.color()[1]=='white'

    def testTurtleIsInUpperLeftHandCorner(self):
        assert self.m.t.pos()==(-190,190), "Turtle position is %d,%d" % \
               (self.m.t.pos()[0],self.m.t.pos()[1])

    def testTurtleMatrixIs0InUpperLeftHandCorner(self):
        assert self.m.matrix[0][0]==0

    def testScreenSize(self):
        assert self.m.s.screensize()==(400,400)

    def testMatrixValueAt(self):
        assert self.m.getMatrixValueAt(-190,190)==0
        
    def testForReset(self):
        assert self.m.reset()==True

        
if __name__=="__main__":
    unittest.main()
