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

    def reset(self):
        self.s = turtle.Screen()
        self.s.window_width = self.size
        self.s.window_height = self.size
        self.s.clear()
        self.s.bgcolor('blue')
        self.t = turtle.Turtle()
        self.t.penup()
        self.s.register_shape("custom",((self.pathWidth/2,self.pathWidth/2),\
                                        (-self.pathWidth/2,self.pathWidth/2),\
                                        (-self.pathWidth/2,-self.pathWidth/2),(self.pathWidth/2,-self.pathWidth/2),\
                                        (self.pathWidth/2,self.pathWidth/2)))
        self.t.shape("custom")
        self.matrix = [[1 for i in range(int(self.size/self.pathWidth))] for j in range(int(self.size/self.pathWidth))]
        self.t.goto(-(self.size/2-self.pathWidth/2),self.size/2-self.pathWidth/2)
        self.matrix[0][0]=EMPTY
        self.home = self.t.pos()

    def getMatrixValueAt(self,pos):
        x = int(int(pos[0]+self.size/2)/self.pathWidth)
        y = int((self.size/2 - pos[1])/self.pathWidth)
        if x < 0 or y < 0 or x > self.size/self.pathWidth-1 or y > self.size/self.pathWidth-1:
            return -1
        else:
            return self.matrix[x][y]

        
