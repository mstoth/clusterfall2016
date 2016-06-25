from Maze import *
import turtle
import unittest

class testMaze(unittest.TestCase):
    
    def setUp(self):
        # this checks for a Maze class
        self.m=Maze()

         
    def testScreenExists(self):
        print "testScreenExists"
        assert type(self.m.s) == turtle._Screen
        assert self.m.s.window_width == 420
        assert self.m.s.bgcolor() == 'blue'

    def testTurtleExists(self):
        assert type(self.m.t) == turtle.Turtle



if __name__=='__main__':
    unittest.main()
