import turtle
class Maze():
    def __init__(self,size=420):
        self.size=size
        self.reset()

    def reset(self):
        self.s = turtle.Screen()
        self.s.window_width = self.size
        self.s.window_height = self.size
        self.s.bgcolor('blue')
        self.t = turtle.Turtle()
        self.t.penup()
        self.matrix = [[1 for i in range(21)] for j in range(21)]
        self.t.goto(-(self.size/2-10),self.size/2-10)
        self.matrix[0][0]=0

    def getMatrixValueAt(self,pos):
        x=int(pos[0]+self.size/2)/20
        y=(self.size/20)-int((pos[1]+self.size/2)/20)-1
        if x < 0 or y < 0 or x > self.size/20-1 or y > self.size/20-1:
            return -1
        v=self.matrix[x][y]
        return v
