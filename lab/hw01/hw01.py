""" Homework 1: Variables & Functions, Control """

from operator import add, sub, mul, neg

def a_sub_abs_b(a, b):
    """Return a-abs(b), but without calling abs.

    >>> a_sub_abs_b(2, 3)
    -1
    >>> a_sub_abs_b(2, -3)
    -1
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_sub_abs_b), re.M)
    ['return h(a, b)']
    """
    if b >= 0:
        h = sub
    else:
        h = add
    # print h(a,b)
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two largest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # and a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return max(x*x+y*y, y*y+z*z, x*x+z*z)

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    result = 0
    i=1
    while i<x:
        if(x%i == 0) and i >= result:
            result = i 
        
        i= i+1
    
    return result

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    

def t():
    "*** YOUR CODE HERE ***"
    print("1")

def f():
    "*** YOUR CODE HERE ***"
    print("2")

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    len = 0
    while 1:
        len = len + 1
        print(x)
        if(x == 1):
            break
        else:
            if(x%2==0):
                x = x//2
            else:
                x= x*3+1
            
    return len
    

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    result = 1 
    while k>0:
        result = result * n
        n= n-1
        k = k-1
        
    return result
    

def double_ones(n):
    """Return true if n has two ones in a row.
    
    >>> double_ones(1)
    False
    >>> double_ones(11)
    True
    >>> double_ones(2112)
    True
    >>> double_ones(110011)
    True
    >>> double_ones(12345)
    False
    >>> double_ones(10101010)
    False
    """
    "*** YOUR CODE HERE ***"
    str_input = str(n)
    len_input = len(str_input)   #get the number of the input bits
    number = 0
    index = 0 
    while (len_input-1)>=0:   
        # str_input = str(n)
        # len_input = len(str_input)
        if (n // (10**(len_input-1)) == 1 ): #judge the highest bit is 1
            index = index + 1
        else:
            index = 0
        n = n - int(n // (10**(len_input-1)))*(10**(len_input-1))  #update input 
        len_input = len_input -1 #update the length of input 
        str_input = str(n) #check the updated input, the length will be changed more than 1 bit if the next bit is 0 in original input
        len_input_2 = len(str_input)
        if( n!= 0 and len_input_2 != len_input):  #do the bit check to prevent the fake tow 1 in a row
            index = 0
            len_input = len_input_2
        if (index == 2): # if there is two 1 in a row, the number will > 0
            index = 0
            number = number + 1
        
    if number > 0:
        return True
    else:
        return False