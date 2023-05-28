# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Camden Warme>
<MTH 420>
<5/21/23>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la

# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = np.linalg.qr(A)
    c=np.dot(Q.T, b)
    x=la.solve_triangular(R,c)
    return x
try:
    print(least_squares(np.array([[1, 0],[0, 1],[0.5, 3]]), np.array([[0,0,1]]).T))
except:
    raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    H=np.load("housing.npy")
    b=H[:, 1].reshape((33, 1))
    A=np.column_stack((H[:, 0].reshape((33, 1)), np.ones(b.shape)))
    x=least_squares(A, b)
    plt.scatter(H[:,0], H[:,1], marker='x')
    plt.plot(H[:, 0],x[0]*H[:, 0]+x[1])
    return x
try: print(line_fit()), plt.show()
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    H=np.load("housing.npy")
    b=H[:, 1].reshape((33, 1))
    x=np.linspace(0, 16, 1600)
    
    A1=np.vander(H[:,0], 4)
    A2=np.vander(H[:,0], 7)
    A3=np.vander(H[:,0],10)
    A4=np.vander(H[:,0], 13)
    
    x1=la.lstsq(A1, b)[0]
    f1=np.poly1d(x1.flatten())
    x2=la.lstsq(A2,b)[0]
    f2=np.poly1d(x2.flatten())
    x3=la.lstsq(A3, b)[0]
    f3=np.poly1d(x3.flatten())
    x4=la.lstsq(A4, b)[0]
    f4=np.poly1d(x4.flatten())
    
    ax1=plt.subplot(221)
    ax2=plt.subplot(222) 
    ax3=plt.subplot(223)
    ax4=plt.subplot(224)
    ax1.scatter(H[:,0], H[:,1], marker='x')
    ax2.scatter(H[:,0], H[:,1],marker='x')
    ax3.scatter(H[:,0], H[:,1],marker='x')
    ax4.scatter(H[:,0], H[:,1],marker='x')
    ax1.plot(x, f1(x))
    ax2.plot(x, f2(x))
    ax3.plot(x, f3(x))
    ax4.plot(x, f4(x))
    plt.show()
try: polynomial_fit()
except:
    raise NotImplementedError("Problem 3 Incomplete")


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
