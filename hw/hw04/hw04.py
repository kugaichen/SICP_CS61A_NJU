""" Homework 4: Data Abstraction and Trees"""

from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree,is_tree

#####################
# Required Problems #
#####################

def couple(lst1, lst2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> lst1 = [1, 2, 3]
    >>> lst2 = [4, 5, 6]
    >>> couple(lst1, lst2)
    [[1, 4], [2, 5], [3, 6]]
    >>> lst3 = ['c', 6]
    >>> lst4 = ['s', '1']
    >>> couple(lst3, lst4)
    [['c', 's'], [6, '1']]
    """
    assert len(lst1) == len(lst2)
    "*** YOUR CODE HERE ***"
    num = 0
    result = []
    while num < len(lst1):
      middle = [lst1[num]] + [lst2[num]]
      result.insert(num, middle)
      num = num + 1 
    return result 

from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    middle = pow(abs(get_lat(city1) - get_lat(city2)),2) +\
      pow(abs(get_lon(city1) - get_lon(city2)),2)
    result = sqrt(middle)
    
    return result
  
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    city3 = make_city('city3', lat, lon)
    distance1 = distance(city1, city3)
    distance2 = distance(city2, city3)
    if distance1 <= distance2:
      return get_name(city1)
    else:
      return get_name(city2)

def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    order_list = []
    def order(t,order_list):
      # print(label(t))
      if t is not None:
        order_list.append(label(t))
        for b in branches(t):
          order(b,order_list)
     
    order(t,order_list)
    # print(order_list) 
    index = 0   
    for x in order_list:
      if x =='nut':
        index = 1 
    if index == 1:
      return True
    else:
      return False
         
def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
      return tree(label(t),[tree(b) for b in values])
    else:
      return tree(label(t),[sprout_leaves(b,values) for b in branches(t)])
      

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    "*** YOUR CODE HERE ***"
    new_label = label(t1) + label(t2)
    res_branch = []
    index = 0
    if is_leaf(t1) == False or is_leaf(t2) == False:   
      while index < len(branches(t1)) and index < len(branches(t2)):
        b1 = branches(t1)[index]
        b2 = branches(t2)[index]
        new_branch = add_trees(b1,b2)
        index = index + 1 
        res_branch = res_branch + [new_branch]
    if index < len(branches(t1)):
      res_branch = res_branch + branches(t1)[index:]  
    if index < len(branches(t2)):
      res_branch = res_branch + branches(t2)[index:]
    
    return tree(new_label,res_branch)
    
    
def bigpath(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigpath(t, 3)
    4
    >>> bigpath(t, 6)
    2
    >>> bigpath(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    helper_list = []
    final_list = []
    def helper(t,helper_list,final_list):
      helper_list = helper_list + [label(t)]
      # print(helper_list)
      sum = 0
      for i in helper_list:
        sum = sum + i 
      if sum >= n:
        final_list.append(1) 
        # print(final_list)
      if is_leaf(t) == False:
        for b in branches(t):
          helper(b,helper_list,final_list)
    
    helper(t,helper_list,final_list)
    result = len(final_list)
    return result
    
 
def bigger_path(t, n):
    """Return the number of paths in t that have a sum larger or equal to n.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> bigger_path(t, 3)
    9
    >>> bigger_path(t, 6)
    4
    >>> bigger_path(t, 9)
    1
    """
    "*** YOUR CODE HERE ***"
    def helper(t,check_list):
      check_list.append(bigpath(t,n))
      for b in branches(t):
        helper(b,check_list)
          
    check_list = []
    helper(t,check_list)
    return sum(check_list)
        

##########################
# Just for fun Questions #
##########################

def fold_tree(t, base_func, merge_func):
    """Fold tree into a value according to base_func and merge_func"""
    "*** YOUR CODE HERE ***"
    if base_func(t):
      return 1
    return merge_func([fold_tree(b,base_func,merge_func)for b in branches(t)])

def count_leaves(t):
    """Count the leaves of a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> count_leaves(t)
    3
    """
    return fold_tree(t, lambda x: is_leaf(x), sum)

def label_sum(t):
    """Sum up the labels of all nodes in a tree.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> label_sum(t)
    15
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal.

    >>> t = tree(1, [tree(2), tree(3, [tree(4), tree(5)])])
    >>> preorder(t)
    [1, 2, 3, 4, 5]
    """
    return fold_tree(t, 'YOUR EXPRESSION HERE', 'YOUR EXPRESSION HERE')
