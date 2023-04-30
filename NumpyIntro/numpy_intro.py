# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name>
<Class>
<Date>
"""
import numpy as np

def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A= np.array([[3, -1, 4], [1, 5, -9]])
    B= np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    return np.dot(A, B)
try:
    print(prob1())
except:
    raise NotImplementedError("Problem 1 Incomplete")


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A=np.array([[3, 1, 4], [1, 5, 9], [-5, 3, 1]])
    return (-1)*np.dot(np.dot(A, A), A)+9*np.dot(A, A)-15*A
try: 
    print(prob2())
except:
    raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A=np.ones((7, 7))
    B=np.tril(-1*np.ones((7, 7)))+np.triu(5*np.ones((7, 7)))+np.diag(-5*np.ones(7))
    ABA=np.dot(np.dot(A, B), A)
    ABA=ABA.astype(np.int64)
    return ABA
try:
    print(prob3())
except:
    raise NotImplementedError("Problem 3 Incomplete")


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    mask = A<0
    A[mask]=0
    return A
try: print(prob4(np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])))
except:
    
    
    raise NotImplementedError("Problem 4 Incomplete")


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    I=np.eye(3)
    A=np.array([[0, 2, 4], [1, 3, 5]])
    B=np.tril(3*np.ones((3, 3)))
    C=-2*np.diag(np.ones(3))
    return  np.hstack((np.vstack((np.zeros((4, 3)), A, B)), np.vstack((np.concatenate((np.zeros((3, 1)), A.T), axis=1), np.zeros((6, 3)))), np.vstack((I, np.zeros((3, 3)), C))))
try: print(prob5())
except:
    raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    row_sum = np.sum(A, axis=1, keepdims=True)
    return A/row_sum
try: 
    print(prob6(np.array([[0,2,7], [1, 1, 5]])))
except:
    raise NotImplementedError("Problem 6 Incomplete")


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")
