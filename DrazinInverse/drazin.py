# drazin.py
"""Volume 1: The Drazin Inverse.
Camden Warme
MTH 420
05/28/23
"""

import numpy as np
from scipy import linalg as la
import scipy

# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    k=index(A)
    x=np.allclose(np.dot(A, Ad), np.dot(Ad, A))
    y=np.allclose(np.dot(np.linalg.matrix_power(A, k+1), Ad), np.linalg.matrix_power(A, k))
    z=np.allclose(np.dot(np.dot(Ad, A), Ad), Ad)
    if (x==True)and(y==True)and(z==True):
        return True
    else: return False
try: print(is_drazin(np.array([[1,3,0,0], [0,1,3,0], [0,0,1,3], [0,0,0,0]]), np.array([[1,-3,9,81], [0,1,-3,-18], [0,0,1,3], [0,0,0,0]]), 1), is_drazin(np.array([[1,1,3], [5,2,6], [-2,-1,-3]]),np.zeros((3,3)), 3))
except:
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    (n,n)=A.shape
    f1 = lambda x: abs(x) > tol
    f2 = lambda x: abs(x) < tol
    T1,Q1,k1=la.schur(A, sort=f1)
    T2,Q2,k2=la.schur(A, sort=f2)
    U=np.hstack((Q1[:,:k1], Q2[:, :n-k1]))
    V=np.dot(la.inv(U), np.dot(A, U))
    Z=np.zeros((n, n))
    if k1 !=0:
        M_inv=la.inv(V[:k1, :k1])
        Z[:k1, :k1]=M_inv
        return np.dot(np.dot(U, Z),la.inv(U))
    else:
        return np.dot(np.dot(U, Z),np.la.inv(U))

        
try: print(drazin_inverse(np.array([[1,3,0,0], [0,1,3,0], [0,0,1,3], [0,0,0,0]]), tol=1e-4))
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    (n,n)=A.shape
    D=np.diag(np.sum(A, axis=1))
    L=D-A
    Draz= la.pinv(L)
    R=np.zeros((n,n))
    for i in range(0, n):
        for j in range(i+1,n):
            R[i,j]=Draz[i,i]+Draz[j,j]-2*Draz[j,i]
            R[j,i]=R[i,j]
    return R
try: print(effective_resistance(np.array([[0,1,0,0],[1,0,1,0], [0,1,0,1], [0,0,1,0]])))
except:  
    raise NotImplementedError("Problem 3 Incomplete")


# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    
    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")
