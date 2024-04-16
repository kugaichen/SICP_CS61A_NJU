container = []
def obtain_mul(t):
                
        if t.is_leaf() == 1 :
            print(1)
            return t.label
        
        else:
            # print(t.branches)
            print('!!!!!')
            for branch in t.branches:
                print(branch.label)
                print('.......')
                if obtain_mul(branch):
                    container.append(t.label * obtain_mul(branch))
                print(container)
                print('xxxxxx')
                
            print(container)
            
            

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
    
    
    
t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
obtain_mul(t)