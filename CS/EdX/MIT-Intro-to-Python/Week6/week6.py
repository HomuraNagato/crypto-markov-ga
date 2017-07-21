class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Wild(X, Y)
print(w1.getX())

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True
        else:
            return False
    
    def __repr__(self):
        return type(self).__name__ + "(" + str(self.getX()) + ", " + str(self.getY()) + ")"
        

c = Coordinate(3, 4)
print(str(c))
print(repr(c))


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, s2):
        dup_s = intSet()
        for i in s2.vals:
            if i in self.vals:
                dup_s.insert(i)
        return str(dup_s)

    def __len__(self):
        return len(self.vals)

s = intSet()
s.insert(2)
s.insert(3)
s.insert(6)

s2 = intSet()
s2.insert(2)
s2.insert(6)

s3 = intSet()
s4 = intSet()

print(str(s))
print(s.intersect(s2))
print(s3.intersect(s4))
print(len(s2))

class Queue(object):
    def __init__(self):
        self.disney = []

    def insert(self, d):
        self.disney.append(d)

    def remove(self):
        try:
            remover = self.disney[0]
            del self.disney[0]
            return remover
        except:
            raise ValueError(' error!')

q = Queue()
q.insert(2)
q.insert(5)
q.insert(1)
print(q.disney)
q.remove()
print(q.disney)
q2 = Queue()
q2.remove()
