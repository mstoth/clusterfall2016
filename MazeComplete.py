import turtle
import random

EMPTY=0
WALL=1
GOAL=2
VISITED=3
FAILED=4
INVALID=5
REVISITED=6

SIZE=420

EAST=2
SOUTH=1
WEST=3
NORTH=0

class Maze(object):
    def __init__(self,size=420):
        self.size=size
        self.home=(-size/2+10,size/2-10)
        self.reset()
        
    def reset(self):
        self.s = turtle.Screen()
        self.s.clearscreen()
        self.s.bgcolor('blue')
        self.s.window_width = self.size
        self.s.window_height = self.size
        self.t = turtle.Turtle()
        self.t.color('blue')        
        self.t.penup()
        self.matrix = [[WALL for i in range(self.size/20)] for j in range(self.size/20)]
        self.t.goto(-(self.size/2-10),self.size/2-10)
        self.t.shape('square')
        self.t.color('green')
        self.t.stamp()
        self.matrix[0][0]=VISITED
        
    def getMatrixValueAt(self,pos):
        x=int(pos[0]+self.size/2)/20
        y=(self.size/20)-int((pos[1]+self.size/2)/20)-1
        # print "x="+str(x); print "y="+str(y)
        if x < 0 or y < 0 or x > self.size/20-1 or y > self.size/20-1:
            return INVALID
        v=self.matrix[x][y]
        return v
    
    def setMatrixValueAt(self,pos,value):
        x=int(pos[0]+self.size/2)/20
        y=(self.size/20)-int((pos[1]+self.size/2)/20)-1
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

    def dig(self,direction):
        oldpos=self.t.pos()
        if direction == EAST:
            if self.t.position()[0]<self.size/2-10:
                if self.getMatrixValueAt((self.t.position()[0]+40,self.t.position()[1])) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]+40,self.t.position()[1]-20)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]+40,self.t.position()[1]+20)) > 0:
                    self.t.goto(self.t.position()[0]+20,self.t.position()[1])
                    self.setMatrixValueAt(self.t.position(),0)
        if direction == SOUTH:
            if self.t.position()[1]>-(self.size/2-10):
                if self.getMatrixValueAt((self.t.position()[0],self.t.position()[1]-40)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]-20,self.t.position()[1]-40)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]+20,self.t.position()[1]-40)) > 0:
                    self.t.goto(self.t.position()[0],self.t.position()[1]-20)
                    self.setMatrixValueAt(self.t.position(),0)
        if direction == WEST:
            if self.t.position()[0]>-(self.size/2-10):
                if self.getMatrixValueAt((self.t.position()[0]-40,self.t.position()[1])) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]-40,self.t.position()[1]-20)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]-40,self.t.position()[1]+20)) > 0:
                    self.t.goto(self.t.position()[0]-20,self.t.position()[1])
                    self.setMatrixValueAt(self.t.position(),0)
        if direction == NORTH:
            if self.t.position()[1]<(self.size/2-10):
                if self.getMatrixValueAt((self.t.position()[0],self.t.position()[1]+40)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]-20,self.t.position()[1]+40)) > 0 and \
                   self.getMatrixValueAt((self.t.position()[0]+20,self.t.position()[1]+40)) > 0:
                    self.t.goto(self.t.position()[0],self.t.position()[1]+20)
                    self.setMatrixValueAt(self.t.position(),0)

        newpos=self.t.pos()
        self.t.color('white')
        self.t.stamp()
        
        
##        if self.getMatrixValueAt(oldpos)==EMPTY:
##            self.setMatrixValueAt(oldpos,VISITED)
##            self.t.goto(oldpos[0],oldpos[1])
##            self.t.color('green')
##            self.t.stamp()
##            self.t.color('white')
##            self.t.goto(newpos[0],newpos[1])
##            
        return self.t.position()

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

    def immediateNeighbors(self):
        p=self.t.position()
        r=[]
        if p[1]+20>(self.size/2-10):
            r.append([self.t.position(),-1])
        else:
            r.append([(p[0],p[1]+20),self.getMatrixValueAt((p[0],p[1]+20))])
        if p[1]-20<-(self.size/2-10):
            r.append([self.t.position(),-1])
        else:
            r.append([(p[0],p[1]-20),self.getMatrixValueAt((p[0],p[1]-20))])
        if p[0]+20>(self.size/2-10):
            r.append([self.t.position(),-1])
        else:
            r.append([(p[0]+20,p[1]),self.getMatrixValueAt((p[0]+20,p[1]))])
        if p[0]-20<-(self.size/2-10):
            r.append([self.t.position(),-1])
        else:
            r.append([(p[0]-20,p[1]),self.getMatrixValueAt((p[0]-20,p[1]))])
        return r

    def travel(self,direction):
        if direction == EAST:
            if self.getMatrixValueAt((self.t.pos()[0]+20,self.t.pos()[1]))==WALL or \
               self.getMatrixValueAt((self.t.pos()[0]+20,self.t.pos()[1]))==INVALID:
                return self.t.pos()
            self.t.goto(self.t.pos()[0]+20,self.t.pos()[1])
        if direction == WEST:
            if self.getMatrixValueAt((self.t.pos()[0]-20,self.t.pos()[1]))==WALL or \
               self.getMatrixValueAt((self.t.pos()[0]-20,self.t.pos()[1]))==INVALID:
                return self.t.pos()
            self.t.goto(self.t.pos()[0]-20,self.t.pos()[1])
        if direction == NORTH:
            if self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]+20))==WALL or \
               self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]+20))==INVALID:
                return self.t.pos()
            self.t.goto(self.t.pos()[0],self.t.pos()[1]+20)
        if direction == SOUTH:
            if self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]-20))==WALL or \
               self.getMatrixValueAt((self.t.pos()[0],self.t.pos()[1]-20))==INVALID:
                return self.t.pos()
            self.t.goto(self.t.pos()[0],self.t.pos()[1]-20)
        if self.getMatrixValueAt(self.t.pos())==EMPTY:
            self.setMatrixValueAt(self.t.pos(),VISITED)
            self.t.color('green')
            self.t.stamp()
        else:
            self.setMatrixValueAt(self.t.pos(),FAILED)
            self.t.color('red')
            self.t.stamp()
        return self.t.pos()

    def emptyNeighbors(self):
        n=self.immediateNeighbors()
        nEmpty=0
        for nn in n:    
            if nn[1]==EMPTY:
                nEmpty += 1
        return nEmpty
    
    def travel2BranchOrWall(self,direction):
        
        if self.immediateNeighbors()[direction][1]==EMPTY:
            oldpos = self.t.pos()
            if oldpos == self.travel(direction):
                return self.t.pos()
            while self.immediateNeighbors()[direction][1]==EMPTY and \
                  self.emptyNeighbors()==1:
                self.travel(direction)
            self.setMatrixValueAt(self.t.pos(),VISITED)
            if self.immediateNeighbors()[direction][1]==GOAL:
                self.t.goto(self.immediateNeighbors()[direction][0])
        return self.t.pos()
        
    def neighbors(self):
        p=self.t.position()
        r=[]
        # North
        if p[1]+40>(self.size/2-10):
            r.append([(p[0],p[1]+40),-1])
        else:
            r.append([(p[0],p[1]+40),self.getMatrixValueAt((p[0],p[1]+40))])
        # South
        if p[1]-40<-(self.size/2-10):
            r.append([(p[0],p[1]-40),-1])
        else:
            r.append([(p[0],p[1]-40),self.getMatrixValueAt((p[0],p[1]-40))])
        # East
        if p[0]+40>(self.size/2-10):
            r.append([(p[0]+40,p[1]),-1])
        else:
            r.append([(p[0]+40,p[1]),self.getMatrixValueAt((p[0]+40,p[1]))])
        # West
        if p[0]-40<-(self.size/2-10):
            r.append([(p[0]-40,p[1]),-1])
        else:
            r.append([(p[0]-40,p[1]),self.getMatrixValueAt((p[0]-40,p[1]))])
        return r

    def generateMaze(self):
        self.makeMaze()
        self.t.goto((self.size/2-10),-(self.size/2-10))
        self.t.color('yellow')
        self.matrix[self.size/20-2][self.size/20-2]=GOAL
        self.t.stamp()
        self.t.color('white')
        self.t.goto(-(self.size/2-10),(self.size/2-10))

    def solve(self):
        if self.getMatrixValueAt(self.t.pos())==GOAL:
            return True
        else:
            savedpos=self.t.pos()
            for d in [EAST,NORTH,WEST,SOUTH]:
                if self.travel2BranchOrWall(d) != savedpos:
                    if self.solve():
                        return True
                    else:
                        self.backtrack(savedpos)

    def backtrack(self,pos):
        self.setMatrixValueAt(self.t.pos(),FAILED)
        if self.t.pos()[0]>pos[0]:
            while self.t.pos()[0]>pos[0]:
                self.travel(WEST)
        elif self.t.pos()[0]<pos[0]:
            while self.t.pos()[0]<pos[0]:
                self.travel(EAST)
        elif self.t.pos()[1]>pos[1]:
            while self.t.pos()[1]>pos[1]:
                self.travel(SOUTH)
        elif self.t.pos()[1]<pos[1]:
            while self.t.pos()[1]<pos[1]:
                self.travel(NORTH)
        self.setMatrixValueAt(self.t.pos(),VISITED)
        
    def solveMaze(self):
        pos=self.t.pos()
        n=self.immediateNeighbors()
        d=[WEST,EAST,SOUTH,NORTH]
        for nn in n:
            dd=d.pop()
            if nn[1]==GOAL:
                self.t.color('green')
                self.t.stamp()
                return True
            if nn[1]==EMPTY:
                self.travel2BranchOrWall(dd)
                if self.solveMaze():
                    return True
                else: # backtrack
                    # print "backtracking"
                    currentPos = self.t.pos()
                    self.setMatrixValueAt(currentPos,FAILED)
                    self.t.color('red')
                    self.t.stamp()
                    if pos[0]>currentPos[0]: # go back EAST
                        [self.travel(EAST) for i in range(pos[0]-currentPos[0])]
                    elif pos[1]>currentPos[1]: # go back NORTH
                        [self.travel(NORTH) for i in range(pos[1]-currentPos[1])]
                    elif pos[0]<currentPos[0]: # go back WEST
                        [self.travel(WEST) for i in range(currentPos[0]-pos[0])]
                    elif pos[1]<currentPos[1]: # Go back SOUTH
                        [self.travel(SOUTH) for i in range(currentPos[1]-pos[1])]
                    self.setMatrixValueAt(self.t.pos(),EMPTY)
                    self.t.color('white')
                    self.t.stamp()
        return False
                    
    def create(self):
        self.makeMaze()
        self.setMatrixValueAt((200,-200),GOAL)        

    def makeMaze(self):
        n=self.neighbors()
        oldpos=self.t.position()
        while len(n)>0:
            nchoice=random.choice(n)
            n.remove(nchoice)
            self.t.goto(oldpos)
            if self.getMatrixValueAt(nchoice[0])==WALL:
                d=self.direction(self.t.position(),nchoice[0])
                self.dig(d)
                self.dig(d)
                self.makeMaze()
