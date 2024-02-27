""" Homework 3: Recursion and Tree Recursion"""

HW_SOURCE_FILE = 'hw03.py'

#####################
# Required Problems #
#####################

def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'number_of_six',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def divide(n):
        if n < 10 and n != 6 :
            return 0 
        elif n < 10 and n == 6:
            return 1 
        elif n % 10 == 6:
            return 1 + divide(n//10)
        else:
            return divide(n//10)
        
    return divide(n)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    5
    >>> pingpong(8)
    4
    >>> pingpong(15)
    3
    >>> pingpong(21)
    5
    >>> pingpong(22)
    6
    >>> pingpong(30)
    10
    >>> pingpong(68)
    0
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    -1
    >>> pingpong(72)
    -2
    >>> pingpong(100)
    6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def index(n):
        if n == 1 :
            return 0 
        elif n%6 == 0 or number_of_six(n)>0:
            return index(n-1) + 1 
        else:
            return index(n-1) + 0 
    
    if n == 1:
        return 1 
    
    elif n>1:
        return pingpong(n-1) + (-1)**index(n-1)
            
            


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digit  s in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    seq = []
    def divide(n,seq):
        if n<10:
            if n not in seq:
                seq.append(n)
            return seq
        else:
            num = n % 10
            if num not in seq: 
                seq.append(num)
            return divide(n//10,seq)

    def check(seq,value):
        start = seq[0]
        if value == 0:
            return 0
        else:
            number = start + value 
            # print(number)
            if number in seq:
                value = value -1 
                return 0 + check(seq,value)
            else: 
                value = value -1 
                return 1 + check(seq,value) 
        
    divide(n,seq)
    seq.reverse()
    # print(seq)
    if seq[0] == seq[-1]:
        return 0
    elif seq[-1] - seq[0] > 0:
        value = seq[-1] - seq[0] - 1 
        return check(seq,value)
        

def count_change(total, next_money):
    """Return the number of ways to make change for total,
    under the currency system described by next_money.

    >>> def chinese_yuan(money):
    ...     if money == 1:
    ...         return 5
    ...     if money == 5:
    ...         return 10
    ...     if money == 10:
    ...         return 20
    ...     if money == 20:
    ...         return 50
    ...     if money == 50:
    ...         return 100
    >>> def us_cent(money):
    ...     if money == 1:
    ...         return 5
    ...     elif money == 5:
    ...         return 10
    ...     elif money == 10:
    ...         return 25
    >>> count_change(15, chinese_yuan)
    6
    >>> count_change(49, chinese_yuan)
    44
    >>> count_change(49, us_cent)
    39
    >>> count_change(49, lambda x: x * 2)
    692
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    container = [1]
    
    def find_largest(n, total, next_money):
        if next_money(n):
            if next_money(n) > total:
                # container.append(n)
                return n
            else: 
                n = next_money(n)
                container.append(n)
                return find_largest(n, total, next_money)
    
    def count_check(total, num, container, length):
        if total == 0 or num == 1 or length == 0:
            return 1 
        else: 
            if total >= num: 
                return count_check(total-num, num, container, length) + count_check(total, last_element(container,length), container, length-1)
            else:
                return count_check(total, last_element(container,length), container, length-1)
    
    def last_element(container,x):
        return container[x-1]         
    
    find_largest(1, total, next_money)
    x = len(container) - 1 
   
    return  count_check(total, container[x], container, x)          
       


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    
    '''
    the mind is so amamzing, you can understand as 3 steps: 
    1. move 'n-1' stacked disks ( move_stack of (n-1)) to the other rod
    2. move the biggest disk from rod 1 to rod 3 as we can think straightforwardly
    3. move the 'n-1' stacked disks to rod 3 
    
    so these 3 steps can obtain the recursive logic
    '''
    if n == 1:
        print_move(start,end)
    else:
        other = 6 - start - end 
        move_stack(n-1, start, other)
        print_move(start,end)
        move_stack(n-1, other, end)
        


def multiadder(n):
    """Return a function that takes N arguments, one at a time, and adds them.
    >>> f = multiadder(3)
    >>> f(5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6) # 5 + 6
    11
    >>> multiadder(4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    >>> from construct_check import check
    >>> # Make sure multiadder is a pure function.
    >>> check(HW_SOURCE_FILE, 'multiadder',
    ...       ['Nonlocal', 'Global'])
    True
    """
    "*** YOUR CODE HERE ***"
    def num(x):
        return x 
    
    if n == 1:
        return num
    else:
        return lambda a:lambda b: multiadder(n-1)(a+b)


##########################
# Just for fun Questions #
##########################


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'


Y = lambda f: (lambda x: x(x))(lambda x: f(lambda z: x(x)(z)))
fib_maker = lambda f: lambda r: 'YOUR_EXPRESSION_HERE'
number_of_six_maker = lambda f: lambda r: 'YOUR_EXPRESSION_HERE'

my_fib = Y(fib_maker)
my_number_of_six = Y(number_of_six_maker)

# This code sets up doctests for my_fib and my_number_of_six.

my_fib.__name__ = 'my_fib'
my_fib.__doc__="""Given n, returns the nth Fibonacci nuimber.

>>> my_fib(0)
0
>>> my_fib(1)
1
>>> my_fib(2)
1
>>> my_fib(3)
2
>>> my_fib(4)
3
>>> my_fib(5)
5
"""

my_number_of_six.__name__ = 'my_number_of_six'
my_number_of_six.__doc__="""Return the number of 6 in each digit of a positive integer n.

>>> my_number_of_six(666)
3
>>> my_number_of_six(123456)
1
"""
