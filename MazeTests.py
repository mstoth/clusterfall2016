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

if __name__=='__main__':
    unittest.main()
