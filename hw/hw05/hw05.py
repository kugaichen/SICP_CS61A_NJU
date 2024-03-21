""" Homework 5: Nonlocal and Generators"""

from ADT import tree, label, branches, is_leaf, print_tree

#####################
# Required Problems #
#####################

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    attempts = []
    def withdraw(value,code):
        nonlocal balance
        if len(attempts) == 3:
            return 'Your account is locked. Attempts: '+ str(attempts)
        if code != password:
            attempts.append(code)
            return 'Incorrect password'
        else:
            if value <= balance:
                balance = balance - value 
                return balance 
            else:
                return 'Insufficient funds'

    return withdraw


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    verificaation = withdraw(0,old_pass)
    if type(verificaation) == str:
        return verificaation
    
    def test_withdraw(num, code):
        if code == new_pass:
            return withdraw(num,old_pass)
        else:
            return withdraw(num,code)
    return test_withdraw
    


def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of all elements in seq. The permutations could be yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    seq = list(seq)
    if len(seq) == 1 :
        yield seq 
    elif len(seq) == 2:
        yield [seq[0],seq[1]]
        yield [seq[1],seq[0]]
    else:
        for i in range(len(seq)):
            res = permutations(seq[:i]+ seq[i+1:])
            for result in res:
                complete = [seq[i]] + result
                yield complete


def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = tree(5, [tree(7, [tree(2)]), tree(8, [tree(3), tree(4)]), tree(5, [tree(4), tree(2)])])
    >>> v = tree('Go', [tree('C', [tree('C')]), tree('A', [tree('S'), tree(6)]), tree('L', [tree(1), tree('A')])])
    >>> type(lookups(k, 4))
    <class 'generator'>
    >>> sorted([f(v) for f in lookups(k, 2)])
    ['A', 'C']
    >>> sorted([f(v) for f in lookups(k, 3)])
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    "*** YOUR CODE HERE ***"
  
    def look_tree(tree,list_tree):
        list_tree.append(label(tree))
        if branches(tree):
            for branch in branches(tree):
                look_tree(branch,list_tree)
                
        return list_tree
    
    def lookup(x):
        list_tree_v=[]
        def unwine(tree):
            look_tree(tree,list_tree_v)
            if index_list:                 
                return list_tree_v[x]
        return unwine
    
    list_tree_k = []
    list = look_tree(k,list_tree_k)
    
    index_list = []
    for i in range(len(list)):
        if list[i] == key:
            index_list.append(i)
     
    f_list =[]
    for x in index_list:
        f_list.append(lookup(x))
        
    f = iter(f_list)
    while 1:
        try:
            yield next(f)
        except:
            break
"""
this program consumes me so much time to think and debug,
the text code -> [f(v) for f in lookups(k, 2)], let me associate with the 
little question in lab05 -> [next(result) for _ in range(10)].
so i chessed that they have the same data structure and function relationship:
1. f needs a function to obtain parameter(tree) -> so there must be a 'def', which receive
parameter(tree),and select exact value to return.
2. lookups(k,2) will output a 'generator type', so function 'lookups' must yield the next function
3. the most wired point is that 'lookups(k,2)' should output a list so can excute the 
code 'f(v) for f in lookups(k,2)' -> and every element in list shoule return the fuction which can 
recieve parameter(tree), but if will using list to yield -> there will have the error''list' object is not callable',
we can not call the list to receive the next function parameter, we need pass the elements into next function,
which lead us care about 'iter' naturally, but this will output the '<class 'list_iterator'>',
so finally i use 'try and except' to output every elment -> 'Warning Hint: 'for f in lookups(k, 2)', 
that will cause more operating complexity because of traversing the single elment in every loop(having one-elment-loop in 
one-elment-loop)

so above is all i thought and encoutered in coding! 

"""                

##########################
# Just for fun Questions #
##########################

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    def helper(i,m):
        num =1 
        while True:
            if num%m == i:
                yield num
            num += 1 
    for i in range(m):
        yield helper(i,m)
                
