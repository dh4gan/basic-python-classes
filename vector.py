import math

class Vector3D(object):
    """3D cartesian vector object for dynamics"""
# Initialising Function
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        s= '3D Vector ( %f, %f, %f)' % (self.x, self.y, self.z)
        return s

# Vector addition
            
    def add(self,other):
        """ Adds another vector"""
        return Vector3D (self.x + other.x, self.y + other.y, self.z + other.z)
            
# Vector subtraction
            
    def subtract(self,other):
        """ Subtracts another vector"""
        return Vector3D (self.x - other.x, self.y - other.y, self.z - other.z)
            
    def scalarmult(self, num):
        """ Multiplies vector by scalar"""
        return Vector3D (num*self.x, num*self.y,num*self.z)

# Magnitude of the Vector
    
    def mag(self):
        """ Takes magnitude of the vector"""
        mag = math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
        return mag

# Scalar Product
            
    def dot(self,other):
        """Returns dot product of two vectors"""
        dotproduct = 0.0
        dotproduct += self.x*other.x
        dotproduct += self.y*other.y
        dotproduct += self.z*other.z
        return dotproduct
    
# Vector Product
    
    
