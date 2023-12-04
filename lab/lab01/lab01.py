def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 ==1 and b % 2 == 1 # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    "*** YOUR CODE HERE ***"
    result = 1
    while n>0:
        result = result * n
        n=n-1
    
    return result
    


def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    "*** YOUR CODE HERE ***"
    if(a>0 and b>0 and c>0) == 1:
        if( a+b>c and a+c>b and b+c>a ) ==1:
            return True
        else:
            return False
    else:
        return False


def number_of_nine(n):
    """Return the number of 9 in each digit of a positive integer n.

    >>> number_of_nine(999)
    3
    >>> number_of_nine(9876543)
    1
    """
    "*** YOUR CODE HERE ***"
    str_num = str(n)
    len_str = len(str_num)
    # print(len_str)
    num = 0
    while len_str>=1:
        comparsion_value = 9*(10**(len_str-1)) # the value if the highest bit = 9
        highest_value = int((n/(10**(len_str-1))))*(10**(len_str-1))   # the value of the highest bit of n
        if comparsion_value == highest_value:
            num = num + 1
        n = n - highest_value
        len_str = len_str - 1
    return num
        
    
    


def min_digit(x):
    """Return the min digit of x.

    >>> min_digit(10)
    0
    >>> min_digit(4224)
    2
    >>> min_digit(1234567890)
    0
    >>> # make sure that you are using return rather than print
    >>> a = min_digit(123)
    >>> a
    1
    """
    "*** YOUR CODE HERE ***"
    str_num = str(x)
    len_str = len(str_num)
    result = 9 #configure result as the biggest 1-bit value in decimal system
    while len_str>=1:
        value_highbits = int(x/(10**(len_str-1))) #the value of thg highest bit of x
        if value_highbits<result:
            result = value_highbits  
        x = x - value_highbits*(10**(len_str-1)) #updata x 
        len_str = len_str - 1 
        
    return result