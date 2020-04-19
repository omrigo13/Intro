# *************** EXERCISE 7 ***************

# **************************************************************
# *********************** Matrix Class *************************
from VectorModule import Vector

class Matrix:
    """
    represents a Matrix in mathematics
    Matrix consists as a tuple of list of Vector objects
    """
    
    def __init__(self, lst):
        """
        builds a new Matrix as tuple and gets a list of Vectors
        :param list lst: list of vectors represents Matrix
        :return: None if its not a legal Matrix or builds a new Matrix as a tuple
        :rtype: None or Matrix object
        """
        if lst == []:
            return None
        size = len(lst[0])
        for i in range(0,len(lst)):
            if not isinstance(lst[i], Vector):
                return None
            if len(lst[i]) != size:
                return None
        self.content = tuple(lst)
        self.shape = (len(lst),size)
        
    def __add__(self, matrix):
        """
        sums 2 Matrixes and return a new Matrix with the new cordinates
        :param Matrix matrix: a Matrix object to add
        :return: a new Matrix object that sums 2 matrixes
        :rtype: Matrix object
        """
        if self.shape != matrix.shape:
            return None
        else:
            new_matrix = [self.content[i] + matrix.content[i] for i in range(self.shape[0])]
        return Matrix(new_matrix)
    
    def transpose(self):
        """
        gets a matrix object and transpose it
        :return: a new Matrix object represents the transpose matrix
        :rtype: Matrix object
        """
        new_matrix = []
        for i in range(0,self.shape[1]):
            new_matrix.append(Vector([self.content[j][i] for j in range(self.shape[0])]))
        return Matrix(new_matrix)
    
    def __mul__(self, matrix):
        """
        gets 2 matrixes and returns multiplyed matrix object
        or None if its impossible
        :param Matrix matrix: a Matrix object to multiply
        :return: a new Matrix object that represents multiplyed Matrix object
        :rtype: Matrix object
        """
        if self.shape[1]!=matrix.shape[0]:
            return None
        else:
            new_matrix = matrix.transpose()
            final_matrix = []
            for i in range(0,self.shape[0]):
                final_matrix.append(Vector([self.content[i]*new_matrix.content[j] for j in range(matrix.shape[1])]))
            return Matrix(final_matrix)