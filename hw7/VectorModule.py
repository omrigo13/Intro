# *************** EXERCISE 7 ***************

# **************************************************************
# *********************** Vector Class *************************
from math import sqrt
from math import degrees
from math import acos

class Vector:
    """
    represents a Vector in mathematics
    vector consists as a tuple of list of integer numbers
    """

    def __init__(self, lst):
        """
        builds a new Vector as tuple and gets a list of integers
        :param list lst: list of integers represnts a vector
        :return: None if its not a legal vector or builds a new Vector as a tuple
        :rtype: None or Vector object
        """
        self.vec = tuple(lst)
        
    def __repr__(self):
        """
        prints the vector object
        """
        return str(self.vec).replace(" ","")
    
    def __len__(self):
        """
        :return: an integer represents the len of the vector object
        :rtype: integer
        """
        return len(self.vec)
    
    def __eq__(self,vector):
        """
        :param Vector vector: a Vector object to check equallity
        :return: True if the 2 Vectors are the same and False otherwise
        :rtype: bool
        """
        return self.vec == vector.vec and len(self) == len(vector)
    
    def __add__(self,vector):
        """
        sums 2 Vectors and return a new Vector with the new cordinates
        :param Vector vector: a Vector object to add
        :return: a new Vector object that sums 2 vectors
        :rtype: Vector object
        """
        if len(self) != len(vector):
            return None
        lst = [self.vec[i] + vector.vec[i] for i in range(len(self))]
        return Vector(lst)
    
    def __neg__(self):
        """
        returns a negative Vector
        :return: a new Vector object represents the negative Vector
        :rtype: Vector object
        """
        vector = [self.vec[i]*-1 for i in range(len(self))]
        return Vector(vector)
    
    def __sub__(self,vector):
        """
        gets 2 vectors and returns subtracting vector object
        :param Vector vector: a Vector object to subtract
        :return: a new Vector object that subtracting 2 vectors
        :rtype: Vector object
        """
        if len(self) != len(vector):
            return None
        lst = [self.vec[i] + (-vector.vec[i]) for i in range(len(self))]
        return Vector(lst)
    
    def __mul__(self,vector):
        """
        gets 2 vectors and returns multiplyed vector object
        or 1 vector and scalar
        :param Vector vector: a Vector object to multiply
        :param integer vector: a scalar integer to multiply
        :return: a new Vector object that represents multiplyed vector object
        :rtype: Vector object
        """
        if isinstance(vector, Vector):
            if len(self) != len(vector):
                return None
            return sum([self.vec[i] * vector.vec[i] for i in range(len(self))])
        return Vector([self.vec[i] * vector for i in range(len(self))])
    
    def __rmul__(self,vector):
        """
        same as mul function, no matter if you multiply scalar and vector
        or vector and scalar
        """
        return self * vector
    
    def __getitem__(self,i):
        """
        return cordinate value by indexing
        :param int i: gets an index of value in vector object
        :return: value of cordinate
        :rtype: integer
        """
        if len(self) == 0:
            if i != 0:
                return None
        if i < 0 or i > len(self)-1:
            return None
        return self.vec[i]
    
    def norm(self):
        """
        :return: returns the sqrt of vector multiply by himself (norm vector value)
        :rtype: float
        """
        return sqrt(self * self)
    
    def angle(self,vector):
        """
        :return: returns the angle between 2 vectors in degrees
        :rtype: float
        """
        if len(self) != len(vector):
                return None
        return degrees(acos((self * vector)/(self.norm() * vector.norm())))