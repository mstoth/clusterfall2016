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
        self.s.register_shape("custom",((int(self.pathWidth/2),int(self.pathWidth/2)),\
                                        (-int(self.pathWidth/2),int(self.pathWidth/2)),\
                                        (-int(self.pathWidth/2),-int(self.pathWidth/2)),(int(self.pathWidth/2),-int(self.pathWidth/2)),\
                                        (int(self.pathWidth/2),int(self.pathWidth/2))))
        self.t.shape("custom")
        self.matrix = [[1 for i in range(int(self.size/self.pathWidth))] for j in range(int(self.size/self.pathWidth))]
        self.t.goto(-(self.size/2-self.pathWidth/2),self.size/2-self.pathWidth/2)
        self.matrix[0][0]=EMPTY
        self.home = self.t.pos()

    def getMatrixValueAt(self,pos):
        x = int(int(pos[0]+int(self.size/2))/self.pathWidth)
        y = int(int(int(self.size/2) - pos[1])/self.pathWidth)
        if x < 0 or y < 0 or x > int(self.size/self.pathWidth)-1 or y > int(self.size/self.pathWidth)-1:
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
        x=int(int(pos[0]+int(self.size/2))/self.pathWidth)
        y=int(self.size/self.pathWidth)-int((pos[1]+int(self.size/2))/self.pathWidth)-1
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
            

##    def tooClose(self,direction):
##        spos = self.t.pos()
##        x=int(int(spos[0]+int(self.size/2))/self.pathWidth)
##        y=int(self.size/self.pathWidth)-int((spos[1]+int(self.size/2))/self.pathWidth)-1
        
##        if direction == EAST:
##            if x==int(self.size/self.pathWidth)-1:
##                return True
##            try:
##                if self.matrix[x+2][y-1] == WALL and self.matrix[x+2][y+1]==WALL and \
##                   self.matrix[x+1][y-1] == WALL and self.matrix[x+1][y+1]==WALL and \
##                   self.matrix[x+2][y] == WALL:
##                    return False
##            except:
##                return True
##            return True
##        if direction == SOUTH:
##            if y==int(self.size/self.pathWidth)-1:
##                return True
##            try:
##                if self.matrix[x+1][y+2] == WALL and self.matrix[x-1][y+2]==WALL and \
##                   self.matrix[x+1][y+1] == WALL and self.matrix[x-1][y+1]==WALL and \
##                   self.matrix[x][y+2] == WALL:
##                    return False
##            except:
##                return True
##            return True
##        if direction == WEST:
##            if x==0:
##                return True
##            try:
##                if self.matrix[x-2][y-1] == WALL and self.matrix[x-2][y+1]==WALL and \
##                   self.matrix[x-2][y] == WALL and self.matrix[x-1][y+1]==WALL and\
##                   self.matrix[x-1][y-1]==WALL:
##                    return False
##            except:
##                return True
##            return True
##        if direction == NORTH:
##            if y==0:
##                return True
##            try:
##                if self.matrix[x][y-2] == WALL and self.matrix[x-1][y-2]==WALL and \
##                   self.matrix[x+1][y-2] == WALL and self.matrix[x-1][y-1]==WALL \
##                   and self.matrix[x+1][y-1]==WALL:
##                    return False
##            except:
##                return True
##            return True

##    def dig(self,direction):
##        oldpos=self.t.pos()
##        if direction == EAST and not self.tooClose(EAST):
##            self.t.goto(oldpos[0]+self.pathWidth,oldpos[1])
##        if direction == SOUTH and not self.tooClose(SOUTH):
##            self.t.goto(oldpos[0],oldpos[1]-self.pathWidth)
##        if direction == WEST and not self.tooClose(WEST):
##            self.t.goto(oldpos[0]-self.pathWidth,oldpos[1])
##        if direction == NORTH and not self.tooClose(NORTH):
##            self.t.goto(oldpos[0],oldpos[1]+self.pathWidth)
##        spos = self.t.pos()      
##        if self.getMatrixValueAt(spos)==WALL:
##            self.setMatrixValueAt(self.t.pos(),EMPTY)
##        else:
##            self.t.goto(oldpos[0],oldpos[1])
##        return self.t.pos()
                        

##    def neighbors(self):
##        p=self.t.position()
##        r=[]
##        # North
##        if p[1]+2*self.pathWidth>(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([(p[0],p[1]+2*self.pathWidth),-1])
##        else:
##            r.append([(p[0],p[1]+2*self.pathWidth),self.getMatrixValueAt((p[0],p[1]+2*self.pathWidth))])
##        # South
##        if p[1]-2*self.pathWidth<-(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([(p[0],p[1]-2*self.pathWidth),-1])
##        else:
##            r.append([(p[0],p[1]-2*self.pathWidth),self.getMatrixValueAt((p[0],p[1]-2*self.pathWidth))])
##        # East
##        if p[0]+2*self.pathWidth>(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([(p[0]+2*self.pathWidth,p[1]),-1])
##        else:
##            r.append([(p[0]+2*self.pathWidth,p[1]),self.getMatrixValueAt((p[0]+2*self.pathWidth,p[1]))])
##        # West
##        if p[0]-2*self.pathWidth<-(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([(p[0]-2*self.pathWidth,p[1]),-1])
##        else:
##            r.append([(p[0]-2*self.pathWidth,p[1]),self.getMatrixValueAt((p[0]-2*self.pathWidth,p[1]))])
##        return r

##    def create(self):
##        self.createNoGoal()
##        self.setMatrixValueAt((int(self.size/2)-(3*int(self.pathWidth/2)),-int(self.size/2) + (3*int(self.pathWidth/2))),GOAL)
        
        
##    def createNoGoal(self):
##        spos=self.t.pos()
##        n=self.neighbors()
##        while len(n)>0:
##            self.t.goto(spos[0],spos[1])
##            nchoice=random.choice(n)
##            n.remove(nchoice)
##            if nchoice[1]==WALL:
##                d=self.direction(self.t.pos(),nchoice[0])
##                if not self.dig(d)==self.dig(d):
##                    self.createNoGoal()
                    
##    def travel(self,direction):
##        if direction == EAST:
##            if self.getMatrixValueAt((self.t.pos()[0]+self.pathWidth,self.t.pos()[1]))==WALL or \
##               self.getMatrixValueAt((self.t.pos()[0]+self.pathWidth,self.t.pos()[1]))==INVALID:
##                return self.t.pos()
##            self.t.goto(self.t.pos()[0]+self.pathWidth,self.t.pos()[1])
##        if direction == WEST:
##            if self.getMatrixValueAt((self.t.pos()[0]-self.pathWidth,self.t.pos()[1]))==WALL or \
##               self.getMatrixValueAt((self.t.pos()[0]-self.pathWidth,self.t.pos()[1]))==INVALID:
##                return self.t.pos()
##            self.t.goto(self.t.pos()[0]-self.pathWidth,self.t.pos()[1])
##        if direction == NORTH:
##            if self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]+self.pathWidth))==WALL or \
##               self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]+self.pathWidth))==INVALID:
##                return self.t.pos()
##            self.t.goto(self.t.pos()[0],self.t.pos()[1]+self.pathWidth)
##        if direction == SOUTH:
##            if self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]-self.pathWidth))==WALL or \
##               self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]-self.pathWidth))==INVALID:
##                return self.t.pos()
##            self.t.goto(self.t.pos()[0],self.t.pos()[1]-self.pathWidth)
##        if self.getMatrixValueAt(self.t.pos())==EMPTY:
##            self.setMatrixValueAt(self.t.pos(),VISITED)
##            self.t.color('green')
##            self.t.stamp()
##        else:
##            self.setMatrixValueAt(self.t.pos(),FAILED)
##            self.t.color('red')
##            self.t.stamp()
##        return self.t.pos()
               
##    def immediateNeighbors(self):
##        p=self.t.position()
##        r=[]
##        if p[1]+self.pathWidth>(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([self.t.position(),-1])
##        else:
##            r.append([(p[0],p[1]+self.pathWidth),self.getMatrixValueAt((p[0],p[1]+self.pathWidth))])
##        if p[1]-self.pathWidth<-(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([self.t.position(),-1])
##        else:
##            r.append([(p[0],p[1]-self.pathWidth),self.getMatrixValueAt((p[0],p[1]-self.pathWidth))])
##        if p[0]+self.pathWidth>(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([self.t.position(),-1])
##        else:
##            r.append([(p[0]+self.pathWidth,p[1]),self.getMatrixValueAt((p[0]+self.pathWidth,p[1]))])
##        if p[0]-self.pathWidth<-(int(self.size/2)-int(self.pathWidth/2)):
##            r.append([self.t.position(),-1])
##        else:
##            r.append([(p[0]-self.pathWidth,p[1]),self.getMatrixValueAt((p[0]-self.pathWidth,p[1]))])
##        return r


##    def emptyNeighbors(self):
##        n=self.immediateNeighbors()
##        nEmpty=0
##        for nn in n:    
##            if nn[1]==EMPTY:
##                nEmpty += 1
##        return nEmpty
    

##    def travel2BranchOrWall(self,direction):
        
##        if self.immediateNeighbors()[direction][1]==EMPTY:
##            oldpos = self.t.pos()
##            if oldpos == self.travel(direction):
##                return self.t.pos()
##            while self.immediateNeighbors()[direction][1]==EMPTY and \
##                  self.emptyNeighbors()==1:
##                self.travel(direction)
##            self.setMatrixValueAt(self.t.pos(),VISITED)
##            if self.immediateNeighbors()[direction][1]==GOAL:
##                self.t.goto(self.immediateNeighbors()[direction][0])
##        return self.t.pos()


##    def solve(self):
##        if self.getMatrixValueAt(self.t.pos())==GOAL:
##            return True
##        else:
##            savedpos=self.t.pos()
##            for d in [EAST,NORTH,WEST,SOUTH]:
##                if self.travel2BranchOrWall(d) != savedpos:
##                    if self.solve():
##                        return True
##                    else:
##                        self.backtrack(savedpos)

##    def backtrack(self,pos):
##        self.setMatrixValueAt(self.t.pos(),FAILED)
##        if self.t.pos()[0]>pos[0]:
##            while self.t.pos()[0]>pos[0]:
##                self.travel(WEST)
##        elif self.t.pos()[0]<pos[0]:
##            while self.t.pos()[0]<pos[0]:
##                self.travel(EAST)
##        elif self.t.pos()[1]>pos[1]:
##            while self.t.pos()[1]>pos[1]:
##                self.travel(SOUTH)
##        elif self.t.pos()[1]<pos[1]:
##            while self.t.pos()[1]<pos[1]:
##                self.travel(NORTH)
##        self.setMatrixValueAt(self.t.pos(),VISITED)


