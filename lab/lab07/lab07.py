""" Lab 07: Special Method, Linked List and Tree"""

#####################
# Required Problems #
#####################

class Complex:
    """Complex Number.

    >>> a = Complex(1, 2)
    >>> a
    Complex(real=1, imaginary=2)
    >>> print(a)
    1 + 2i
    >>> b = Complex(-1, -2)
    >>> b
    Complex(real=-1, imaginary=-2)
    >>> print(b)
    -1 + -2i
    >>> print(a + b)
    0 + 0i
    >>> print(a * b)
    3 + -4i
    >>> print(a)
    1 + 2i
    >>> print(b) # a and b should not be changed
    -1 + -2i
    """
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    "*** YOUR CODE HERE ***"
    def __repr__(self):
        # return('{0} + {1}i'.format(self.real,self.imaginary))
        return 'Complex(real={0}, imaginary={1})'.format(self.real,self.imaginary)
    
    def __str__(self) -> str:
        return('{0} + {1}i'.format(self.real,self.imaginary)) 
    
    def __add__(self,other):
        nx,ny = self.real,self.imaginary
        mx,my = other.real,other.imaginary
        
        return Complex(nx+mx, ny+my)
    
    def __mul__(self,other):
        nx,ny = self.real,self.imaginary
        mx,my = other.real,other.imaginary
        
        return Complex(nx*mx-ny*my,nx*my+ny*mx)

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(0)
    >>> s
    Link(0)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(8760)
    Link(8, Link(7, Link(6, Link(0))))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not steal chicken!") if any([r in cleaned for r in ["str", "repr", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"
    def get_length(num):
        if num == 0:
            return 0 
        return 1 + get_length(num // 10 )
    
    index = get_length(n) -1 
   
    list = []
    if n<10:
        list.append(n)
    else:
        while 1:
            if n // 10**index > 0:
                x = n//10**index
                list.append(x)
                if n > 10 and n % 10 ** index == 0:
                    list.append(0)
                n = n - x * 10 ** index
                index = index - 1
                
            else:
                break
    
    # print(list)
    def generate_list(list):
        first = list[0]
        # print(first)
        if list[1:]:
            other = list[1:]
            # print(other)

            return Link(first,generate_list(other))
        
        else:
            return Link(first)
    
    return generate_list(list)

        

def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings.

    >>> kirito_to_string = make_to_string("[", "|-]-->", "", "[]")
    >>> eugeo_to_string = make_to_string("(", " . ", ")", "()")
    >>> lst = Link(1, Link(2, Link(3, Link(4))))
    >>> kirito_to_string(lst)
    '[1|-]-->[2|-]-->[3|-]-->[4|-]-->[]'
    >>> kirito_to_string(Link.empty)
    '[]'
    >>> eugeo_to_string(lst)
    '(1 . (2 . (3 . (4 . ()))))'
    >>> eugeo_to_string(Link.empty)
    '()'
    """
    "*** YOUR CODE HERE ***"
    undo_lst = []
    def undo_tree(link):
        if link == Link.empty:
            return '{0}'.format(empty_repr)
        else:
        
            while link.rest is not link.empty:
                undo_lst.append(link.first)
                link = link.rest
            
            undo_lst.append(link.first)
        
            # print(undo_lst)
            print('\'',end='')
            for x in undo_lst:
                print(front,end='')
                print(x,end='')
                print(mid,end='')
            print(empty_repr,end='')
            for x in range(len(undo_lst)):
                print(back,end='')
            print('\'',end='')
    return undo_tree

def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    
    # container = []
    # def obtain_mul(t):
                
    #     if t.is_leaf() == 1 :
    #         return t.label
        
    #     else:
    #         for branch in t.branches:
    #             if obtain_mul(branch):
    #                 container.append(t.label * obtain_mul(branch))
    
    if not t.is_leaf():
        for branch in t.branches:
            cumulative_mul(branch)
            t.label = t.label * branch.label 
 


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label.

    >>> t1 = Tree(6)
    >>> prune_small(t1, 2)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_small(t2, 1)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2), Tree(3)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_small(t3, 2)
    >>> t3
    Tree(6, [Tree(1), Tree(3, [Tree(1), Tree(2)])])
    """
    "*** YOUR CODE HERE ***"
    # my method
    # if t.is_leaf() == 1 or len(t.branches) <= n :
    #     pass
    # else:
     
    #     index= []  
    #     for b in t.branches:
    #         index.append(b.label)
    #     index.sort()
    #     # print(index)
    #     index = index[:n]
    #     # print(index)
    
    #     for b in t.branches:
    #         flag = 0 
    #         for ele in index:
    #             if b.label == ele:
    #                 flag = 1 
    #                 break
    #         if flag == 0 :
    #             t.branches.remove(b)
        
    #     for b in t.branches:
    #         prune_small(b,n)    

    # easy method
    while len(t.branches) > n:
        largest = max(b.label for b in t.branches)
        for b in t.branches:
            if b.label == largest:
                t.branches.remove(b)
        
    for b in t.branches:
        prune_small(b,n)
        

#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
