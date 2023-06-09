# montecarlo_integration.py
"""Volume 1: Monte Carlo Integration.
Camden Warme
MTH 420
6/9/23
"""
import numpy as np
from scipy import linalg as la

# Problem 1
def ball_volume(n, N=10000):
    """Estimate the volume of the n-dimensional unit ball.

    Parameters:
        n (int): The dimension of the ball. n=2 corresponds to the unit circle,
            n=3 corresponds to the unit sphere, and so on.
        N (int): The number of random points to sample.

    Returns:
        (float): An estimate for the volume of the n-dimensional unit ball.
    """
    points = np.random.uniform(-1,1,(n,N))
    lengths=la.norm(points, axis=0)
    num_within=np.count_nonzero(lengths<1)
    return (2**n)*(num_within/N)
try: print(ball_volume(2))
except:
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def mc_integrate1d(f, a, b, N=10000):
    """Approximate the integral of f on the interval [a,b].

    Parameters:
        f (function): the function to integrate. Accepts and returns scalars.
        a (float): the lower bound of interval of integration.
        b (float): the lower bound of interval of integration.
        N (int): The number of random points to sample.

    Returns:
        (float): An approximation of the integral of f over [a,b].

    Example:
        >>> f = lambda x: x**2
        >>> mc_integrate1d(f, -4, 2)    # Integrate from -4 to 2.
        23.734810301138324              # The true value is 24.
    """
    points=np.random.uniform(a,b,(1,N))
    return (b-a)*(1/N)*np.sum(f(points))
try:
    f = lambda x: x**0
    print(mc_integrate1d(f, -4, 2))
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def mc_integrate(f, mins, maxs, N=10000):
    """Approximate the integral of f over the box defined by mins and maxs.

    Parameters:
        f (function): The function to integrate. Accepts and returns
            1-D NumPy arrays of length n.
        mins (list): the lower bounds of integration.
        maxs (list): the upper bounds of integration.
        N (int): The number of random points to sample.

    Returns:
        (float): An approximation of the integral of f over the domain.

    Example:
        # Define f(x,y) = 3x - 4y + y^2. Inputs are grouped into an array.
        >>> f = lambda x: 3*x[0] - 4*x[1] + x[1]**2

        # Integrate over the box [1,3]x[-2,1].
        >>> mc_integrate(f, [1, -2], [3, 1])
        53.562651072181225              # The true value is 54.
    """
    n=len(mins)
    points=np.random.uniform(0,1,(n,N))
    scale=np.array([x-y for x,y in zip(maxs,mins)])
    arr_sc=np.diag(scale)
    points_sc=np.dot(arr_sc,points)
    arr_mins=np.array(mins).reshape((n,1))
    final_pts=points_sc+arr_mins
    V=np.prod(scale)
    columns=final_pts.T.tolist()
    f_sum=sum([f(i) for i in columns])
    f_max=min([f(i) for i in columns])
    return V*f_sum/N, f_max
try:
    f=lambda x: x[0]+x[1]-x[3]*x[2]**2
    print(mc_integrate(f, [-1,-2,-3,-4], [1,2,3,4]))
except:
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Let n=4 and Omega = [-3/2,3/4]x[0,1]x[0,1/2]x[0,1].
    - Define the joint distribution f of n standard normal random variables.
    - Use SciPy to integrate f over Omega.
    - Get 20 integer values of N that are roughly logarithmically spaced from
        10**1 to 10**5. For each value of N, use mc_integrate() to compute
        estimates of the integral of f over Omega with N samples. Compute the
        relative error of estimate.
    - Plot the relative error against the sample size N on a log-log scale.
        Also plot the line 1 / sqrt(N) for comparison.
    """
    raise NotImplementedError("Problem 4 Incomplete")
