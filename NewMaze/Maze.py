import random
import turtle

SIZE = 400
PATHWIDTH = 20
PW2 = PATHWIDTH/2

class Maze():
    def __init__(self):
        self.s = turtle.Screen()
        self.s.screensize(SIZE,SIZE)
        self.t = turtle.Turtle()
        self.s.bgcolor('blue')
        self.s.register_shape("custom",((PW2, PW2),(PW2, -PW2),\
                                        (PW2,-PW2),(-PW2,-PW2),\
                                        (-PW2,-PW2),(-PW2,PW2),\
                                        (-PW2,PW2), (PW2,PW2)))
        self.t.shape("custom")
        self.t.color('white')
        self.t.penup()

    def reset(self):
        self.matrix = [[1 for i in range(int(SIZE/PATHWIDTH))] \
                          for i in range(int(SIZE/PATHWIDTH))]
        self.t.goto(-SIZE/2+PW2,SIZE/2-PW2)
        self.matrix[0][0]=0


        
    def getMatrixValueAt(self,x,y):
        xi = int((x+SIZE/2-PW2)/PATHWIDTH)
        yi = int(-(y-(SIZE/2-PW2))/PATHWIDTH)
        return self.matrix[xi][yi]
    
