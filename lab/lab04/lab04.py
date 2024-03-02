# The constructor and selectors of the mobile

def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

# The constructor and selectors of the arm

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]

# The constructor and selectors of the planet

def planet(size):
    """Construct a planet of some size.
    
    >>> planet(5)
    ['planet', 5]
    """
    assert size > 0
    "*** YOUR CODE HERE ***"
    result = ['planet']
    result.append(size)
    return result

def size(w):
    """Select the size of a planet.
    
    >>> p = planet(5)
    >>> size(p)
    5
    """
    assert is_planet(w), 'must call size on a planet'
    "*** YOUR CODE HERE ***"
    return w[1]

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

# examples and usage

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)

def total_weight(m):
    """Return the total weight of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(arm(3, t), arm(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(arm(1, v), arm(1, w)))
    False
    >>> balanced(mobile(arm(1, w), arm(1, v)))
    False
    """
    assert is_mobile(m)
    "*** YOUR CODE HERE ***"
    def result():
        if is_planet(end(right(m))) and is_planet(end(left(m))):
            left_weight = total_weight(end(left(m)))
            right_weight = total_weight(end(right(m)))
            left_length = length(left(m))
            right_length = length(right(m))
            # weight = left_weight + right_weight
            if left_length * left_weight == right_length * right_weight:
                return True
            else:
                return False
        
        elif is_mobile(end(right(m))) and is_mobile(end(left(m))):
            left_balanced =  balanced(end(left(m)))  
            right_balanced = balanced(end(right(m)))
            if left_balanced * total_weight(end(left(m))) * length(left(m)) == \
                right_balanced * total_weight(end(right(m))) * length(right(m)):
                    return True
            else:
                return False
            
            
        elif is_mobile(end(left(m))): 
            left_balanced =  balanced(end(left(m)))  
            if left_balanced * total_weight(end(left(m))) * length(left(m)) == \
                total_weight(end(right(m))) * length(right(m)):
                    return True
            else: 
                return False
        
        elif is_mobile(end(right(m))):
            right_balanced = balanced(end(right(m)))
            if right_balanced * total_weight(end(right(m))) * length(right(m)) ==\
                total_weight(end(left(m))) * length(left(m)):
                    return True
            else:
                return False
               
    result = result()
    # print(result)
    if result == True:
        return True
    else: 
        return False
    



from ADT import tree, label, branches, is_leaf, print_tree

def totals_tree(m):
    """Return a tree representing the mobile/planet with its total weight at the root.

    >>> t, u, v = examples()
    >>> print_tree(totals_tree(t))
    3
      2
      1
    >>> print_tree(totals_tree(u))
    6
      1
      5
        3
        2
    >>> print_tree(totals_tree(v))
    9
      3
        2
        1
      6
        1
        5
          3
          2
    """
    '''
     t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
               
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    '''
    assert is_mobile(m) or is_planet(m)
    "*** YOUR CODE HERE ***"
    if is_planet(m):
        return tree(total_weight(m))

    return tree(total_weight(m), [totals_tree(i) for i in [end(left(m)), end(right(m))]])


def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    result = []
    def helper(t):
        if t is not None:
            result.append(label(t))
            for b in branches(t):
                helper(b)
    helper(t)
    return result
        
             
def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word.

    >>> greetings = tree('h', [tree('i'),
    ...                        tree('e', [tree('l', [tree('l', [tree('o')])]),
    ...                                   tree('y')])])
    >>> print_tree(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    "*** YOUR CODE HERE ***"
    
    flag = 0 
    word_list = [x for x in word]
    length = len(word_list)
    index_word = 0
    
    if word_list[index_word] == label(t):
        flag = flag + 1 
        while length > flag:
            index_word = index_word + 1 
            for b in branches(t):
               if word_list[index_word] == label(b):
                   flag = flag + 1 
                   t = b           
                   break   
        
    if flag == length:
        return True
    else:
        return False
                

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    length = len(lst)
    num = 0
    while num < length:
        if lst[num] == entry:
            num = num + 1
            lst.insert(num, elem)
            num = num + 1 
        else:
            num = num + 1 
    
    return lst
        
        
            
