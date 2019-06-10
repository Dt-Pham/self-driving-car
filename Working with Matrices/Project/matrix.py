import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            return self.g[0][0]
        
        return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        return sum([self.g[i][i] for i in range(self.h)])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        if self.h == 1:
            return 1 / self.determinant() * identity(1)
        
        return 1 / self.determinant() * (self.trace() * identity(self.h) - self)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_tranpose = zeroes(self.w, self.h)
        for i in range(self.w):
            for j in range(self.h):
                matrix_tranpose[i][j] = self.g[j][i]
        return matrix_tranpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrix_sum = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix_sum[i][j] = self.g[i][j] + other[i][j]
        
        return matrix_sum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        matrix_neg = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                matrix_neg[i][j] = -self.g[i][j]
        return matrix_neg

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + (-other)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if (self.w != other.h):
            raise(ValueError, "Dimension error") 
        
        matrix_mul = zeroes(self.h, other.w)
        for i in range(self.h):
            for j in range(other.w):
                matrix_mul[i][j] = sum([self[i][k] * other[k][j] for k in range(self.w)])

        return matrix_mul

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            matrix_new = zeroes(self.w, self.h)
            for i in range(self.w):
                for j in range(self.h):
                    matrix_new[i][j] = self.g[i][j] * other    
            return matrix_new
        
        raise(ValueError, "Left operand is not a number") 

