from Maze import *
import turtle
import unittest

class testMaze(unittest.TestCase):
    
    def setUp(self):
        # this checks for a Maze class
        self.m=Maze(SIZE)

