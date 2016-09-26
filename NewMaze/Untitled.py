    def testTurtleIsWhite(self):
        assert self.m.t.color()[0]=='white' and self.m.t.color()[1]=='white'

    def testThatMatrixUpperLeftHandCornerIs0(self):
        assert self.m.matrix[0][0]==0

    def testScreenIs400x400(self):
        assert self.m.s.screensize()==(400,400), "Screen Size is %d,%d" % \
               (self.m.s.screensize()[0] , self.m.s.screensize()[1])


    def testReset(self):
        assert self.m.reset()==None

    def testGetMatrixValueAt(self):
        self.m.reset()
        xpos = -190
        ypos = 190
        assert self.m.getMatrixValueAt((xpos,ypos))==0








        self.matrix[0][0]=0  # we start from the upper left hand corner

    def reset(self):
        pass
        # do this in class

    def getMatrixValueAt(self,pos):
        x = int((pos[0]+200)/20)
        y = int((200 - pos[1])/20)
        if x < 0 or y < 0 or x > int(200)-1 or y > int(200)-1:
            return -1
        else:
            return self.matrix[x][y]
