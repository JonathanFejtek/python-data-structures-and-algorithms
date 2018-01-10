class EmptyBSTError:
    """Exception class used when deleting an item from an empty BST."""
    pass


class EmptyValue:
    """Represents the root value of an empty BST."""
    pass


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and < all items stored in its right subtree.

    Attributes:
    - root (object): the root value stored in the BST, or EmptyValue
                     if the tree is empty
    - left (BinarySearchTree): the left subtree, or None if the tree is empty
    - right (BinarySearchTree): the right subtree, or None if the tree is empty
    """
    def __init__(self, root=EmptyValue):
        """ (BinarySearchTree, object) -> NoneType

        Create a new binary search tree with a given root value.
        An empty BST has its root attribute set to EmptyValue.
        """
        self.root = root    # root value
        if self.is_empty():
            # Set left and right to nothing,
            # because this is an empty binary tree.
            self.left = None
            self.right = None
        else:
            # Set left and right to be new empty trees.
            # Note that this is different than setting them to None!
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()


    def is_empty(self):
        """ (BinarySearchTree) -> bool

        Return True if this tree is empty.
        Empty trees are identified by having root value EmptyValue.
        """
        return self.root is EmptyValue
    
    
    def print_tree(self, depth=0):
        """ (BinarySearchTree, int) -> NoneType

        Print all of the items in this tree,
        where the root is printed before its left and right subtrees,
        and every value is indented to show its depth.
        """
        if not self.is_empty():
            print(depth * '  ' + str(self.root))
            self.left.print_tree(depth + 1)
            self.right.print_tree(depth + 1)
            
    
    def __contains__(self, item):
        """ (BinarySearchTree, object) -> bool
        Return True if this tree contains item.
        """
        if self.is_empty():
            return False
        elif item == self.root:
            return True
        elif item < self.root:
            return self.left.__contains__(item)
            # Or, return item in self.left
        else:
            return self.right.__contains__(item)


    def count_all(self, item):
        """ (BinarySearchTree, object) -> int
        Return the number of times item appears in this tree.
        (Return 0 if this tree is empty.)
        """
        if self.is_empty():
            return 0
        
        else:
            if self.root == item:
                return 1 + self.left.count_all(item) + self.right.count_all(item)
            
            else:
                return 0 + self.left.count_all(item) + self.right.count_all(item)

          
    def count_all2(self, item):
        """ (BinarySearchTree, object) -> int
        Return the number of times item appears in this tree.
        (Return 0 if this tree is empty.)
        """
        if self.is_empty():
            return 0
        
        else:
            if self.root == item:
                return 1 + self.left.count_all2(item)
            
            elif item < self.root:
                return 0 + self.left.count_all2(item)
            
            else:
                return 0 + self.right.count_all2(item)
    
    
    def range(self, low, high):
        """ (BinarySearchTree, object, object) -> int

        Precondition: low and high can be compared with items in this tree.

        Return the number of items in this tree whose value is
        between low and high, inclusive.
        """
        
        ###Naive implementation!
        
        #if empty, no items in specified range
        if self.is_empty():
            return 0
        
        #if this item is in range add and recurse
        elif high >= self.root >= low:
            return 1 + self.left.range(low,high) + self.right.range(low,high)
        
        #if this item is not in range, add and recurse
        else:
            return 0 + self.left.range(low,high) + self.right.range(low,high)
        

    def insert(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Insert item into this tree in the correct location.
        Do not change positions of any other nodes.
        """
        if self.is_empty():
            # Make new leaf node.
            # Note that self.left and self.right cannot be None if the
            # tree is non-empty! (This is one of our invariants.)
            self.root = item
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
            
        elif item <= self.root:
            self.left.insert(item)
            
        else:
            self.right.insert(item)


    def delete(self, item):
        """ (BinarySearchTree, object) -> NoneType

        Remove item from this tree.
        Do nothing is this tree doesn't contain item.
        """
        if not self.is_empty():
            if self.root == item:
                self.delete_root()
            elif item < self.root:
                self.left.delete(item)
            else:
                self.right.delete(item)
    
    
    def delete_root(self):
        """ (BinarySearchTree) -> NoneType
        Remove the root node of this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        
        elif self.left.is_empty() and self.right.is_empty():
            self.root = EmptyValue
            self.left = None
            self.right = None
            
        elif not self.left.is_empty():
            self.root = self.left.extract_max()
            
        elif not self.right.is_empty():
            self.root = self.right.extract_min()


    def extract_max(self):
        """ (BinarySearchTree) -> object

        Remove and return the maximum item stored in this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        elif self.right.is_empty():
            temp = self.root
            # Copy left subtree to self, because root node is removed.
            # Note that self = self.left does NOT work!
            self.root = self.left.root
            self.right = self.left.right
            self.left = self.left.left
            return temp
        else:
            return self.right.extract_max()


    def extract_min(self):
        """ (BinarySearchTree) -> object
        Remove and return the minimum item stored in this tree.
        Raise EmptyBSTError if this tree is empty.
        """
        if self.is_empty():
            raise EmptyBSTError
        
        elif self.left.is_empty():
            temp = self.root
            self.root = self.right.root
            self.right = self.right.right
            self.left = self.left.left
            return temp
        else:
            return self.left.extract_min()
        

    def list_range(self, low, high):
        """ (BinarySearchTree, object, object) -> list

        Precondition: low and high can be compared with items in this tree.

        Return a sorted list of the items in this tree whose value is
        between low and high, inclusive.
        Note: the returned list should include any duplicates
        that appear in this tree.
        """
        
        if self.is_empty():
            return []
        
        elif high >= self.root >= low:
            return self.left.list_range(low, high) + [self.root] + self.right.list_range(low, high)
        
        else:
            return self.left.list_range(low, high) + [] + self.right.list_range(low, high)
        

    def pre_order(self):
        
        if self.is_empty():
            return []
        
        else:
            return [self.root] + self.left.pre_order() + self.right.pre_order()
    
    
    def in_order(self):
        
        if self.is_empty():
            return []
        
        else:
            return  self.left.in_order() + [self.root] + self.right.in_order()
    
    
    def post_order(self):
        
        if self.is_empty():
            return []
        
        else:
            return  self.left.post_order() + self.right.post_order() + [self.root]
    
    
    def multiply_leaves(self):
        
        if self.is_empty():
            return 1
        
        elif self.left.is_empty() and self.right.is_empty():
            return self.root        
        
        else:
            return 1 * self.left.multiply_leaves() * self.right.multiply_leaves()
        

    def remove_smallest(self):
        
        if self.is_empty():
            raise IndexError
        
        elif self.left.is_empty():
            temp = self.root
            self.root = self.right.root
            self.left = self.right.left
            self.right = self.right.right
            return temp
        
        else:
            self.left.remove_smallest()
            
    
    def list_leaves(self):
        
        if self.is_empty():
            return []
        
        elif self.right.is_empty() and self.left.is_empty():
            return [self.root]
        
        else:
            return self.left.list_leaves() + [] + self.right.list_leaves()
        
    
    def rotate_cc(self):
        
        # copy right
        temp = BinarySearchTree()
        temp.root = self.right.root
        temp.left = self.right.left
        temp.right = self.right.right
        
        # copy self, set right to temp's left tree
        self_copy = BinarySearchTree()
        self_copy.root = self.root
        self_copy.left = self.left
        self_copy.right = temp.left
        
        # set old "self" to be temp's left
        temp.left = self_copy
        
        # set new self to be temp 
        self.root = temp.root
        self.right = temp.right
        self.left = temp.left

       
    def size(self):
        
        if self.is_empty():
            return 0
        
        else:
            return self.left.size() + 1 + self.right.size()

       
    def list_duplicates(self):
        
        if self.is_empty():
            return []
        
        elif self.left.is_empty() and self.right.is_empty():
            return []
        
        elif not self.left.is_empty():
            left_tree = self.left.in_order()
            
            if left_tree[-1] == self.root:
                return  self.left.list_duplicates() + [self.root] + self.right.list_duplicates()
            
            else:
                return self.left.list_duplicates() + self.right.list_duplicates()
        
        else:
            return self.left.list_duplicates() + self.right.list_duplicates()


    def list_range2(self,low,high):
        
        if self.is_empty():
            return []
        
        else:
            if(high >= self.root >= low):
                lst = [self.root]
            
            else:
                lst = []
                
            return (self.left.list_range2(low,high) + lst +
                   self.right.list_range2(low,high))


    def map_f(self,f):
        
        if not self.is_empty():
            self.root = f(self.root)
            self.left.map_f(f)
            self.right.map_f(f)

     
    def multiply_non_leaves(self):
        
        if self.is_empty():
            return 1
        
        elif self.right.is_empty() and self.left.is_empty():
            return 1
        
        else:
            return self.root * self.left.multiply_non_leaves() * self.right.multiply_non_leaves()


    def depth(self):
        
        if self.is_empty():
            return 0
        
        elif self.left.is_empty() and self.right.is_empty():
            return 1
        
        else:
            depth_left = 1 + self.left.depth()
            depth_right = 1 + self.right.depth()
            
            return max([depth_left,depth_right])
        
        
def copy(bt):
    
    if bt.is_empty():
        return BinarySearchTree()
    
    else:
        new_bt = BinarySearchTree(bt.root)
        bt.left = copy(bt.left)
        bt.right = copy(bt.right)
        return new_bt 


def copy_into(bt1, bt2):
    
    if bt1.is_empty():
        if not bt2.is_empty():
            bt2.delete_root()
            copy_into(bt1, bt2)
            
    elif bt2.is_empty():
        bt2.root = bt1.root
        bt2.left = BinarySearchTree()
        bt2.right = BinarySearchTree()
        copy_into(bt1.left,bt2.left)
        copy_into(bt1.right,bt2.right)
        
    else:
        if bt1.root != bt2.root:
            bt2.root = bt1.root
            
        copy_into(bt1.left,bt2.left)
        copy_into(bt1.right,bt2.right)

        
def change_root(tree, item):
    
    if tree.is_empty():
        tree.root = item
    
    else:
        tree.root = item
        if not tree.left.is_empty():
            if (tree.root < tree.left.root):
                node_to_insert = tree.left.extract_max()
                tree.right.insert(node_to_insert)
                print(item)
                change_root(tree,item)
            
        if not tree.right.is_empty():
            if tree.root >= tree.right.root:
                node_to_insert = tree.right.extract_min()
                tree.left.insert(node_to_insert)
                change_root(tree,item)
                

def is_BST(bt):
    
    if bt.is_empty():
        return True
    
    elif bt.right.is_empty() and bt.left.is_empty():
        return True
    
    elif bt.right.is_empty():
        return ((bt.root >= bt.left.root) and is_BST(bt.left))
    
    elif bt.left.is_empty():
        return ((bt.root < bt.right.root) and is_BST(bt.right))
    
    else:
        return ((bt.root >= bt.left.root) and (bt.root < bt.right.root)
                and is_BST(bt.left) and is_BST(bt.right))


def is_BST2(bt):
    
    if bt.is_empty():
        return True
    
    elif bt.right.is_empty() and bt.left.is_empty():
        return True
    
    elif not bt.left.is_empty() and get_max(bt.left) > bt.root:
        return False
    
    elif not bt.right.is_empty() and get_min(bt.right) <= bt.root:
        return False
    
    elif not is_BST(bt.left) or not is_BST(bt.right):
        return False
    
    else:
        return True


def get_max(bt):
    
    if bt.is_empty():
        pass
    
    elif bt.right.is_empty():
        return bt.root
    
    else:
        return get_max(bt.right)

  
def get_min(bt):
    
    if bt.is_empty():
        pass
    
    elif bt.left.is_empty() and bt.right.is_empty():
        return bt.root
    
    elif bt.left.is_empty():
        return bt.root
    
    else:
        return get_min(bt.left)

       
def find_duplicates(bst):
    
    if bst.is_empty():
        return 0
    
    else:
        if bst.root == bst.left:
            duplicates = 1
        else:
            duplicates = 0
            
        return find_duplicates(bst.left) + duplicates + find_duplicates(bst.right)

    
def count(item, bst):
    
    if bst.is_empty():
        return 0
    
    elif item == bst.root:
        return 1 + count(item, bst.left)
    
    elif item < bst.root:
        return 0 + count(item, bst.left)
    
    else:
        return 0 + count(item, bst.right)

    
def flatten(bt):
    
    if bt.is_empty():
        return (None,None)
    
    elif bt.left.is_empty() and bt.right.is_empty():
        return (LinkedList([bt.root]),None)
    
    elif bt.left.is_empty():
        return (LinkedList([bt.root]), flatten(bt.right)[1])
    
    elif bt.right.is_empty():
        return (LinkedList([bt.root]),flatten(bt.left)[0])
    
    else:
        ll = LinkedList([bt.root])
        ll.prev = flatten(bt.left)[0]
        ll.next = flatten(bt.right)[1]
        return (ll.prev,ll.next)


def kth_largest(bst, k):
    
    if bst.is_empty():
        pass
    
    elif k == bst.right.size() + 1:
        return bst.root
    
    elif k > bst.right.size() + 1:
        return kth_largest(bst.left, k - (bst.right.size() + 1))
    
    else:
        return kth_largest(bst.right, k)

  
def list_items_gt_10(bst):
    
    if bst.is_empty():
        return []
    
    elif bst.root >= 10:
        return  list_items_gt_10(bst.left) + [bst.root] + list_items_gt_10(bst.right)
    
    elif bst.root < 10:
        return [] + list_items_gt_10(bst.right)
    

def insert_list(bst,lst):
    
    if bst.is_empty():
        if not len(lst) == 0:
            bst.root = lst.pop()
            bst.left = BinarySearchTree()
            bst.right = BinarySearchTree()
            insert_list(bst,lst)
    
    else:
        left_items = []
        right_items = []
        
        for item in lst:
            if item <= bst.root:
                left_items.append(item)
            else:
                right_items.append(item)
                
        insert_list(bst.left, left_items)
        insert_list(bst.right, right_items)

        
def count_nodes(bt):
    
    if bt.is_empty():
        return 0
    
    else:
        return 1 + count_nodes(bt.left) + count_nodes(bt.right)


def count_nodes_valid(bt):
    
    if bt.is_empty():
        return 0
    
    elif bt.left.is_empty() and bt.right.is_empty():
        return 1
    
    elif bt.right.is_empty():
        return 1
    
    elif bt.left.is_empty():
        return 0
    
    else:
        return count_nodes_valid(bt.left) + 1 + count_nodes_valid(bt.right)
    
def is_complete(bt):
    
    if bt.is_empty():
        return True
    
    else:
        return count_nodes_valid(bt) == count_nodes(bt)



