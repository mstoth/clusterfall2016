import turtle
class Maze():
    def __init__(self,size=420):
        self.s = turtle.Screen()
        self.size=size
        self.s.window_width = self.size
        self.s.window_height = self.size
