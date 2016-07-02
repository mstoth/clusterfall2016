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
        self.t.shape("square")
        self.matrix = [[1 for i in range(self.size/self.pathWidth)] for j in range(self.size/self.pathWidth)]
        self.t.goto(-(self.size/2-self.pathWidth/2),self.size/2-self.pathWidth/2)
        self.matrix[0][0]=EMPTY

    def getMatrixValueAt(self,pos):
        x = int(pos[0]+self.size/2)/self.pathWidth
        y=(self.size/2 - pos[1])/self.pathWidth        
        if x < 0 or y < 0 or x > self.size/self.pathWidth-1 or y > self.size/self.pathWidth-1:
            return -1
        else:
            return self.matrix[x][y]

    def direction(self,pos1,pos2):
        p1x=int(pos1[0]); p1y=int(pos1[1]); p2x=pos2[0]; p2y=pos2[1]
        if p1x==p2x and p1y==p2y:
            return 0
        """ returns the direction from position 1 to position 2 """
        if p1x==p2x: # x position the same, either NORTH or SOUTH
            if p2y>p1y: # NORTH
                return NORTH
            else:
                return SOUTH
        else:
            if p2x>p1x: # EAST
                return EAST
            else:
                return WEST

    def setMatrixValueAt(self,pos,value):
        x=int(pos[0]+self.size/2)/self.pathWidth
        y=(self.size/self.pathWidth)-int((pos[1]+self.size/2)/self.pathWidth)-1
        try:
            self.matrix[x][y]=value
        except:
            return False
        spos = self.t.pos()
        self.t.goto(pos)
        if value == WALL:
            self.t.color('blue')
            self.t.stamp()
        elif value == VISITED:
            self.t.color('green')
            self.t.stamp()
        elif value == FAILED:
            self.t.color('red')
            self.t.stamp()
        elif value == GOAL:
            self.t.color('yellow')
            self.t.stamp()
        else:
            self.t.color('white')
            self.t.stamp()
        self.t.goto(spos)
        return True
            

    def tooClose(self,direction):
        spos = self.t.pos()
        x=int(spos[0]+self.size/2)/self.pathWidth
        y=(self.size/self.pathWidth)-int((spos[1]+self.size/2)/self.pathWidth)-1
        
        if direction == EAST:
            if x==self.size/self.pathWidth-1:
                return True
            try:
                if self.matrix[x+1][y-1] == WALL and self.matrix[x+1][y+1]==WALL and \
                   self.matrix[x+1][y] == WALL:
                    return False
            except:
                return True
            return True
        if direction == SOUTH:
            if y==self.size/self.pathWidth-1:
                return True
            try:
                if self.matrix[x+1][y+1] == WALL and self.matrix[x-1][y+1]==WALL and \
                   self.matrix[x][y+1] == WALL:
                    return False
            except:
                return True
            return True
        if direction == WEST:
            if x==0:
                return True
            try:
                if self.matrix[x-1][y-1] == WALL and self.matrix[x-1][y+1]==WALL and \
                   self.matrix[x-1][y] == WALL:
                    return False
            except:
                return True
            return True
        if direction == NORTH:
            if y==0:
                return True
            try:
                if self.matrix[x][y-1] == WALL and self.matrix[x-1][y-1]==WALL and \
                   self.matrix[x+1][y-1] == WALL:
                    return False
            except:
                return True
            return True

    def dig(self,direction):
        oldpos=self.t.pos()
        if direction == EAST:
            self.t.goto(oldpos[0]+self.pathWidth,oldpos[1])
            toooClose = self.tooClose(EAST)               
        if direction == SOUTH:
            self.t.goto(oldpos[0],oldpos[1]-self.pathWidth)
            toooClose = self.tooClose(SOUTH)
        if direction == WEST:
            self.t.goto(oldpos[0]-self.pathWidth,oldpos[1])
            toooClose = self.tooClose(WEST)
        if direction == NORTH:
            self.t.goto(oldpos[0],oldpos[1]+self.pathWidth)
            toooClose = self.tooClose(NORTH)
        spos = self.t.pos()
        
        if self.getMatrixValueAt(spos)==WALL and not toooClose:
            self.setMatrixValueAt(self.t.pos(),EMPTY)
        else:
            self.t.goto(oldpos[0],oldpos[1])
        return self.t.pos()
                        

    def neighbors(self):
        p=self.t.position()
        r=[]
        # North
        if p[1]+2*self.pathWidth>(self.size/2-self.pathWidth/2):
            r.append([(p[0],p[1]+2*self.pathWidth),-1])
        else:
            r.append([(p[0],p[1]+2*self.pathWidth),self.getMatrixValueAt((p[0],p[1]+2*self.pathWidth))])
        # South
        if p[1]-2*self.pathWidth<-(self.size/2-self.pathWidth/2):
            r.append([(p[0],p[1]-2*self.pathWidth),-1])
        else:
            r.append([(p[0],p[1]-2*self.pathWidth),self.getMatrixValueAt((p[0],p[1]-2*self.pathWidth))])
        # East
        if p[0]+2*self.pathWidth>(self.size/2-self.pathWidth/2):
            r.append([(p[0]+2*self.pathWidth,p[1]),-1])
        else:
            r.append([(p[0]+2*self.pathWidth,p[1]),self.getMatrixValueAt((p[0]+2*self.pathWidth,p[1]))])
        # West
        if p[0]-2*self.pathWidth<-(self.size/2-self.pathWidth/2):
            r.append([(p[0]-2*self.pathWidth,p[1]),-1])
        else:
            r.append([(p[0]-2*self.pathWidth,p[1]),self.getMatrixValueAt((p[0]-2*self.pathWidth,p[1]))])
        return r

    def create(self):
        spos=self.t.pos()
        n=self.neighbors()
        while len(n)>0:
            self.t.goto(spos[0],spos[1])
            nchoice=random.choice(n)
            n.remove(nchoice)
            if nchoice[1]==WALL:
                d=self.direction(self.t.pos(),nchoice[0])
                if not self.dig(d)==self.dig(d):
                    self.create()
                    
                

