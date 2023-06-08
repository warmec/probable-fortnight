# standard_library.py
"""Python Essentials: The Standard Library.
Camden Warme
MTH 420
4/21/2023
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return min(L), max(L), sum(L)/len(L)
try:
    print(prob1([1, 2, 3, 4, 5]))
except:
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    #testing integers
    five = int(5)
    five2=five
    five=five+1
    if five==five2:
        print("Integers are mutable")
    else:
        print("Integers are immutable")
    #testing strings
    word = "blake"
    word2=word
    word += "rules"
    if word==word2:
        print("Strings are mutable")
    else:
        print("Strings are immutable")
    #testing lists
    blah=['x', 'y']
    blahh=blah
    blahh.append('z')
    if blah==blahh:
        print("Lists are mutable")
    else:
        print("Lists are immutable")
    #testing tuples
    print("Since no syntax allows tuples to be modified, they must be immutable")
    #testing sets
    myset={1111, 11, 111}
    myset2=myset
    myset.add(111111111111)
    if myset==myset2:
        print("Sets are mutable")
    else:
        print("Sets are immutable")
try:
    prob2()
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
"""Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' .

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
def hypot(a, b):
    import numpy as np
    import calculator as c
    return np.sqrt(c.sum(c.product(a, a), c.product(b, b)))
try:
    print(hypot(3, 4))
except:
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    import itertools
    power_set=[]
    for i in range(len(A)+1):
        for j in list(itertools.combinations(A, i)):
            power_set.append(list(j))
    return [set(subset) for subset in power_set]
try:
    print(power_set('hi'))
    
except:
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
