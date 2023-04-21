
# python_intro.py
"""Python Essentials: Introduction to Python.
Camden Warme
MTH 420
4/10/2023
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")
    
# Problem 2
""" Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
def sphere_volume(r):
    return 4/3*3.14159*r**3
try:   
    print(sphere_volume(1))
except:
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
""" Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
def isolate(a, b, c, d, e):
    return print(a,"   ",b,"   ",c, d, e)
try:
    isolate(1,2,3,4,5)
except: 
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
""" Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.
    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
def first_half(my_string):
    import math
    length=len(my_string)
    cutoff=math.floor(length/2)
    return my_string[0:cutoff]
try: 
    print(first_half("cocobolo"))
except:
    raise NotImplementedError("Problem 4 Incomplete")
    
""" Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
def backward(my_string):
    length=len(my_string)
    for i in range(length):
        if (i==0):
            my_string2=my_string[length-1-i]
        else:
            my_string2=my_string2+my_string[length-1-i]
    return my_string2
try: 
    print(backward("cocobolo"))
except:

    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
""" Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
def list_ops():
    animals=['bear', 'ant', 'cat', 'dog']
    animals.append('eagle')
    animals[2]='fox'
    animals.remove(animals[1])
    animals[0], animals[3] = animals[3], animals[0] 
    animals[0], animals[1] = animals[1], animals[0] 
    animals.remove('eagle')
    animals.insert(1, 'hawk')
    animals[3]= animals[3]+'hunter'
  
    return animals
try:
    print(list_ops())
except:
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
""" Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
def pig_latin(word):
    length=len(word)
    vowels={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    if word[0] in vowels:
        word=word+'yay'
    else:    
        word=word[1:length]+word[0]+'ay'
    return word
try:
    print(pig_latin('Indigo'))
except:
    raise NotImplementedError("Problem 6 Incomplete")


# Problem 7
def palindrome():
    """Find and retun the largest panindromic number made from the product
    of two 3-digit numbers."""

    p_products=[0]
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i*j
            str_prod = str(product)
            rev_str_prod = backward(str_prod)
            if rev_str_prod==str_prod:
                p_products.append(product)
    p_prod_bts = sorted(p_products, reverse=True)
    
    return p_prod_bts[0]
try:
    print(palindrome())
except:
            
    
    
    raise NotImplementedError("Problem 7 Incomplete")

# Problem 8
""" Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
def alt_harmonic(n):
    numbers = [((-1)**(i+1))/i for i in range(1,n+1)]
    return sum(numbers)
try:
    print(alt_harmonic(100))
except:
    raise NotImplementedError("Problem 8 Incomplete")
