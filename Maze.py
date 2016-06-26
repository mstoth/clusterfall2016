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
