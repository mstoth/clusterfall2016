import turtle
EMPTY=0

class Maze():
    def __init__(self,size=420,pathWidth=20):
        self.size=size
        self.pathWidth=pathWidth
        self.reset()

    def reset(self):
        self.s = turtle.Screen()
        self.s.window_width = self.size
        self.s.window_height = self.size
        self.s.bgcolor('blue')
        self.t = turtle.Turtle()
        self.t.penup()
        self.matrix = [[1 for i in range(self.size/self.pathWidth)] for j in range(21)]
        self.t.goto(-(self.size/2-self.pathWidth/2),self.size/2-self.pathWidth/2)
        self.matrix[0][0]=EMPTY

    def getMatrixValueAt(self,pos):
        x = int(pos[0]+self.size/2)/self.pathWidth
        y=(self.size/2 - pos[1])/self.pathWidth
        print x,y
        
        if x < 0 or y < 0 or x > self.size/self.pathWidth-1 or y > self.size/self.pathWidth-1:
            return -1
        else:
            return self.matrix[x][y]
