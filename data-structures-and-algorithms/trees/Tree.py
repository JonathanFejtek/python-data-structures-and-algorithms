import random;


class EmptyValue:
    pass

class Tree:
    
    def __init__(self,root=EmptyValue):
        self.root = root;
        self.children = [];
        
        
    def is_empty(self):
        """ (Tree) -> bool
        Return True if self is empty.
        """
        return self.root is EmptyValue
    

    def add_subtrees(self, new_trees):
        """ (Tree, list of Tree) -> NoneType
        Add the trees in new_tree as subtrees of this tree.
        """
        self.subtrees = self.subtrees + new_trees
        

    def size(self):
        """ (Tree) -> int
        Return the number of nodes contained in this tree.
        """
        if self.is_empty():
            return 0
        else:
            size = 1
            for subtree in self.subtrees:
                size += subtree.size()
            return size
    

    def print_tree(self):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees.
        """
        if not self.is_empty():
            # This prints the root item before all of the subtrees.
            print(self.root)
            for subtree in self.subtrees:
                subtree.print_tree()

        # Or alternately, simply call
        # self.print_tree_indent()
    

    def print_tree_indent(self, depth=0):
        """ (Tree) -> NoneType

        Print all of the items in this tree,
        where the root is printed before all of its subtrees,
        and every value is indented to show its depth.
        """
        if not self.is_empty():
            print(depth * '  ' + str(self.root))
            for subtree in self.subtrees:
                subtree.print_tree_indent(depth + 1)
    
    
    def delete_root(self):
        """ (Tree) -> NoneType
        Remove the root item of this tree.
        """
        
        if len(self.subtrees) == 0:
            # Base case when empty or just one node
            self.root = EmptyValue
        else:
            # Note: this removes a whole subtree from
            # self.subtrees!
            
            #1.Pop last child
            temp = self.subtrees.pop()
            #2.Reassign members
            #2a.Replace root of this tree with child's root
            self.root = temp.root
            #2b.Replace children of this tree with child's children
            self.subtrees = self.subtrees + temp.subtrees
            
            
    def delete_item(self, item):
        """ (Tree, object) -> bool
        Delete *one* occurrence of item from this tree.
        Return True if item was deleted, and False otherwise.
        """
        if self.is_empty():
            return False
        
        elif self.root == item:
            #base case: item to delete is this tree's item.
            self.delete_root()
            return True
        
        else:
            for subtree in self.subtrees:
                # Try to delete item from current subtree
                # If it works, return!
                if subtree.delete_item(item):
                    # If the subtree is now empty, remove it!
                    if subtree.is_empty():
                        self.subtrees.remove(subtree)
                    return True
            return False
        
    
    def __contains__(self, item):
        """ (Tree, object) -> bool
        Return True if item is in this tree.
        """
        if self.is_empty():
            return False
        
        elif item == self.root:
            return True
        
        else:
            for subtree in self.subtrees:
                if subtree.__contains__(item):
                    return True
            
            return False
        
    
    def get_branching_factor(self):
        """ (Tree) -> int
        Return the average branching factor of this tree.
        Remember to ignore all 0's coming from leaves in
        this calculation.
        Return 0 if this tree is empty or consists of just
        a single root node.
        """
        
        return self.get_branching_factor_helper()[0]/self.get_branching_factor_helper()[1]

    def get_branching_factor_helper(self):
        """ (Tree) -> (int, int)
        Return a tuple (x,y) where
        x is the total branching factor of all non-leaf nodes in this tree, and
        y is the total number of non-leaf nodes in this tree.
        """
        
        if self.is_empty() or self.subtrees == []:
            return (0,0)
        
        else:
            bf, non_leaf_nodes = len(self.subtrees), 1
            
            for subtree in self.subtrees:
                bf += subtree.get_branching_factor_helper()[0]
                non_leaf_nodes += subtree.get_branching_factor_helper()[1]
                
            return (bf, non_leaf_nodes)
        
    def list_all(self):
        """ (Tree) -> list of objects
        Return a list of all items in this tree.
        """
        if self.is_empty():
            return []
        
        else:
            lst = [self.root]
            for subtree in self.subtrees:
                lst += subtree.list_all()
            
            return lst
        
        
    def delete_leaf(self):
        """
        (Tree) -> object
        Delete and return a leaf (first in traversal).
        """
        if self.subtrees == []:
            temp = self.root
            self.root = EmptyValue
            return temp
        
        else:
            for subtree in self.subtrees:
                leaf = subtree.delete_leaf()
                if subtree.is_empty():
                    self.subtrees.remove(subtree)
                return leaf
            
            
    def delete_item2(self,item):
        """ (Tree,object) -> bool
        Alternative implementation for delete_item.
        """
        ## if tree is empty, return False
        if self.is_empty():
            return False
        
        ## if item is equal to root, and has no children
        elif self.root == item and (self.subtrees == []):
            self.root = EmptyValue
            return True
        
        ## if item is equal to root and tree has children    
        elif self.root == item:
            self.root = self.delete_leaf()
            return True
        
        ## recursive call   
        else:
            for subtree in self.subtrees:
                if subtree.delete_item(item):
                    return True
            
            return False
    
    
    def add_leaves(self):
        """ (Tree) -> number
        Return the numerical value of every leaf in this tree.
        """
        if self.is_empty():
            return 0
        
        elif (self.subtrees == []):
            if(type(self.root) is float or type(self.root) is int):
                return self.root
            
            else:
                return 0;
        
        else:
            sum_ = 0
            for subtree in self.subtrees:
                sum_ += subtree.add_leaves()
            
            return sum_
    
    
    def list_leaves(self):
        """ (Tree) -> list of objects
        Return a list containing every leaf in this tree.
        """        
        
        if self.is_empty():
            return []
        
        elif not self.subtrees:
            return [self.root]
        
        else:
            leaves = []
            for subtree in self.subtrees:
                leaves += subtree.list_leaves()
                
            return leaves
    
    
    def list_non_leaves(self):
        """ (Tree) -> list of objects
        Return a list containing every non-leaf in this tree.
        """
        if self.is_empty():
            return []
        
        else:
            if self.subtrees:
                non_leaves = [self.root]
            
            else:
                non_leaves = []
                
            for subtree in self.subtrees:
                non_leaves += subtree.list_non_leaves()
                
            return non_leaves
    
        
    def get_height(self):
        """
        """
        
        if self.is_empty():
            return 0
        
        elif not self.subtrees:
            return 1
        
        else:
            subtree_h = []
            for subtree in self.subtrees:
                subtree_height = 1 + subtree.get_height()
                subtree_h += [subtree_height]
            
            return max(subtree_h)
    
    
    def get_height2(self):
        """
        """
        
        if self.is_empty():
            return 0
        
        else:
            subtree_h = [1]
            for subtree in self.subtrees:
                subtree_h += [1 + subtree.get_height()]
            
            return max(subtree_h)
    
    
    def purge_clones(self):
        """
        """
    
        if self.is_empty() or not self.subtrees:
            pass
    
        else:
            for subtree in self.subtrees:
                if subtree.root == self.root:
                    #subtree.purge_clones()
                    subtree.delete_root()
                    tree.purge_clones()
                else:
                    subtree.purge_clones()
    
    
    def insert(self, item):
        """ (Tree, object) -> NoneType
        """
        if self.is_empty():
            self.root = item
            
        elif not self.subtrees:
            self.subtrees.append(Tree(item))
        
        else:
            choice = random.randint(1,3)
            if choice == 3:
                self.subtrees.append(Tree(item))
            
            else:
                index = random.randint(0,len(self.subtrees)-1)
                self.subtrees[index].insert(item)
    
    
    def __eq__(self, other):
        """ (Tree, Tree) -> bool

        Return True if this tree and the other tree are equal trees.
        """
        if self.is_empty() and other.is_empty():
            return True
        
        elif self.is_empty() or other.is_empty():
            return False
        
        elif (self.root != other.root):
            return False
        
        else:
            for sub, oth_sub in zip(self.subtrees,other.subtrees):
                if not sub.__eq__(oth_sub):
                    return False
            
            return True
    
    
    def common_items(self, other):
        
        if self.is_empty() and other.is_empty():
            return []
        
        elif self.is_empty() or other.is_empty():
            return []
        
        else:
            if (self.root == other.root):
                common = [self.root]
            else:
                common = []
            
            for subtree_self, subtree_other in zip(self.subtrees, other.subtrees):
                common += subtree_self.common_items(subtree_other)
            
            return common
    

def count_internal_nodes(tree):
    
    if tree.is_empty():
        return 0
    
    elif tree.subtrees == []:
        return 0
    
    else:
        internal_nodes = 1
        for subtree in tree.subtrees:
            internal_nodes += count_internal_nodes(subtree)
        
        return internal_nodes
    
def count_less_than_depth(tree,d):
    
    if tree.is_empty():
        return 0
    
    elif(d == 1):
        return 1
    
    else:
        nodes_at_depth = 1
        for subtree in tree.subtrees:
            nodes_at_depth += count_less_than_depth(subtree,d-1)
        
        return nodes_at_depth
    
    
def count_less_than_depth2(tree,d):
    
    if tree.is_empty():
        return 0
    
    elif(d >=1 ):
        nodes_at_depth = 1
        for subtree in tree.subtrees:
            nodes_at_depth += count_less_than_depth(subtree,d-1)
        
        return nodes_at_depth
            
    else:
        return 0 
        
    
def count_greater_than_depth(tree,d):
    
    if tree.is_empty():
        return 0
    
    else:
        if (d <= 1):
            nodes_at_depth = 1
        else:
            nodes_at_depth = 0
        
        for subtree in tree.subtrees:
            nodes_at_depth += count_greater_than_depth(subtree,d-1)
        
        return nodes_at_depth
    
def count_item(tree,item):
    
    if tree.is_empty():
        return 0
    
    else:
        if tree.root == item:
            count = 1
        else:
            count = 0
        
        for subtree in tree.subtrees:
            count += count_item(subtree,item)
        
        return count
    
def sum_up(tree):
    
    if tree.is_empty():
        return 0
    
    else:
        s = tree.root
        for subtree in tree.subtrees:
            s += sum_up(subtree)
        
        return s

def count_duplicates(tree):
    
    items = tree.list_all()
    duplicates = 0
    seen = []
    for item in items:
        if count_item(tree,item) > 1 and item not in seen:
            duplicates += count_item(tree,item) - 1
            seen.append(item)
        
    return duplicates
    

def make_binary(tree):
    
    if tree.is_empty():
        pass
    
    elif len(tree.subtrees) <= 2:
        pass
    
    else:
        extra_trees = []
        while len(tree.subtrees) > 2:
            extra_tree = tree.subtrees.pop()
            new_tree = Tree(extra_tree.root)
            new_tree.subtrees = extra_tree.subtrees
            extra_trees.append(new_tree)
            
        for extra_tree in extra_trees:
            tree.subtrees[0].subtrees += [extra_tree]
            
        for subtree in tree.subtrees:
            make_binary(subtree)
            
def limit_branches(tree, d):
    
    if tree.is_empty():
        pass
    
    elif len(tree.subtrees) <= d:
        pass
    
    else:
        extra_trees = []
        while len(tree.subtrees) > d:
            extra_tree = tree.subtrees.pop()
            new_tree = Tree(extra_tree.root)
            new_tree.subtrees = extra_tree.subtrees
            extra_trees.append(new_tree)
            
        for extra_tree in extra_trees:
            tree.subtrees[0].subtrees += [extra_tree]
            
        for subtree in tree.subtrees:
            limit_branches(subtree,d)
            
            
def is_binary(tree):
    
    if tree.is_empty():
        return True
    
    elif len(tree.subtrees) > 2:
        return False
    
    else:
        for subtree in tree.subtrees:
            if is_binary(subtree) is False:
                return False
        
        return True
    
def satisfies_d_branching(tree,d):
    
    if tree.is_empty():
        return True
    
    elif len(tree.subtrees) > d:
        return False
    
    else:
        for subtree in tree.subtrees:
            if satisfies_d_branching(subtree,d) is False:
                return False
        
        return True

def deepen(tree):
    
    if tree.is_empty():
        pass
    
    elif not tree.subtrees:
        expand_tree = Tree(tree.root)
        tree.subtrees.append(expand_tree)
    
    else:
        expand_tree = Tree(tree.root)
        expand_tree.subtrees = tree.subtrees
        tree.subtrees = [expand_tree]
        for subtree in expand_tree.subtrees:
            deepen(subtree)
            
def common_items(tree1,tree2):
    
    if tree1.is_empty() or tree2.is_empty():
        return 0
    
    else:
        if tree1.root in tree2:
            common = 1
        else:
            common = 0
            
        for subtree in tree1.subtrees:
            common += common_items(subtree,tree2)
            
        return common  