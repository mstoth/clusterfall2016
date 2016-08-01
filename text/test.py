
class shape(object):
    def __init__(self):
        self.color='blue'

class triangle(shape):
    def __init__(self):
        self.numSides = 3
        super shape

class square(shape):
    def __init__(self):
        self.numSides = 4
        super shape

