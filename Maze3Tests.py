from Maze3 import *
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
        self.m=Maze3(SIZE)

if __name__=="__main__":
    unittest.main()
    
