# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name>
<Class>
<Date>
"""
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    arr = np.random.normal(size=(n, n))
    mean = np.mean(arr, axis=1, keepdims=True)
    return np.var(mean)
try:
    print( var_of_means(100))
except:
    raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    n=np.arange(1, 11)*100
    yarr=np.array([var_of_means(i) for i in n])
    return plt.plot(n,yarr)
try: prob1(), plt.show(), plt.clf() 
except:
    raise NotImplementedError("Problem 1 Incomplete")
    
# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x=np.linspace(-2*np.pi, 2*np.pi, 100)
    y1=np.sin(x)
    y2=np.cos(x)
    y3=np.arctan(x)
    return plt.plot(x, y1), plt.plot(x, y2), plt.plot(x, y3)
try: prob2(), plt.show(), plt.clf() 
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 0.99, 300)
    x2 = np.linspace(1.01, 6, 500)
    y1= np.array([1/(i-1) for i in x1])
    y2= np.array([1/(i-1) for i in x2])
    return plt.plot(x1, y1, 'm--', lw=4), plt.plot(x2, y2, 'm--', lw=4), plt.xlim(-2, 6), plt.ylim(-6, 6)
try: prob3(), plt.show(), plt.clf()
except:
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x=np.linspace(0, 2*np.pi, 200)
    
    ax1=plt.subplot(221)
    ax2=plt.subplot(222) 
    ax3=plt.subplot(223)
    ax4=plt.subplot(224)
    ax1.set_title("sin(x)")
    ax2.set_title("sin(2x)")
    ax3.set_title("2sin(x)")
    ax4.set_title("2sin(2x)")
    plt.suptitle("Some Sinusoids :)")
    return ax1.plot(x, np.sin(x), 'g-'), ax2.plot(x, np.sin(2*x), 'r--'), ax3.plot(x, 2*np.sin(x), 'b--'), ax4.plot(x, 2*np.sin(2*x), 'm:'), plt.axis([0, 2*np.pi, -2, 2])
try: prob4(), plt.show(), plt.clf()
except:
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x=np.linspace(-2*np.pi, 2*np.pi)
    y=x
    X, Y = np.meshgrid(x, y)
    Z=np.sin(X)*np.sin(Y)/(X*Y)
    ax1=plt.subplot(121)
    ax2=plt.subplot(122)
    cont =ax1.contour(X, Y, Z, 20, cmap="viridis")
    heat =ax2.pcolormesh(X, Y, Z, cmap="magma", shading="auto")
    cbar1 = plt.colorbar(cont, ax=ax1)
    cbar2 = plt.colorbar(heat, ax=ax2) 
    return cont, heat, cbar1, cbar2
try: prob6(), plt.show()
except:
    raise NotImplementedError("Problem 6 Incomplete")
