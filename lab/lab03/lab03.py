""" Lab 3: Recursion and Tree Recursion """

this_file = __file__


def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n - 2 <= 0: 
        return n
    else:
        n = n - 2
        return (n + 2 + skip_add(n))


def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(this_file, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    if n==1: 
        return term(n)
    else:
        return term(n) + summation(n-1,term)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    def divisorn(a,b,n):
        if a % n == 0 and b % n == 0:
            return n 
        elif n == 1 : 
            return n
        else: 
            return divisorn(a,b,n-1)
    if a>=b:
        base = b
    else: 
        base = a 
    return divisorn(a,b,base)
        


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m==1 or n==1 :
        return 1 
    elif m!= 1 and n!=1:
        return paths(m-1,n)+paths(m,n-1)


def max_subseq(n, l):
    """
    Return the maximum subsequence of length at most l that can be found in the given number n.
    For example, for n = 20125 and l = 3, we have that the subsequences are
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015
        025
        125
    and of these, the maximum number is 225, so our answer is 225.

    >>> max_subseq(20125, 3)
    225
    >>> max_subseq(20125, 5)
    20125
    >>> max_subseq(20125, 6) # note that 20125 == 020125
    20125
    >>> max_subseq(12345, 3)
    345
    >>> max_subseq(12345, 0) # 0 is of length 0
    0
    >>> max_subseq(12345, 1)
    5
    """
    "*** YOUR CODE HERE ***"
    # that question i can not find the answer, so i did it as my own mind.
    # using list and recursion to complete that
    seq = []
    def divid(n):
        if n<10:
            seq.append(n)
        else:
            seq.append(n%10)
            return divid(n//10)
        # print(seq)
        
    def find(start,seq,l,seq_result):
        if start == (len(seq) - 1):
            seq_result.append(seq[-1])
            return seq_result
        else:
            k1 = 0
            i1 = 1
            for i in range(start,len(seq)-l+1):
                if seq[i] > k1:
                    k1 = seq[i]
                    i1 = i 
                    # print (k1)
                    # print (i1)
            seq_result.append(k1)
            return find(i1+1,seq,l-1,seq_result)
    
    divid(n)
    seq.reverse()
    
    if l>= len(seq):
        for i in seq:
            print(i,end='')
            
    elif l == 0:
        print(0)
            
    elif l == 1:
        k = 0
        for i in range(0,5):
            if seq[i] > k:
                k = seq[i]
            # print(seq[i])
        print(k)
        
    else:      
        seq_result = []
        for i in find(0, seq, l, seq_result):
            print(i,end='')
        
            
        
