class Node:
    """A node in a linked list.

    Attributes:
    - item (object): the data stored in this node
    - next (Node): the next Node in the list, or None if this
                   is the last Node
    """

    def __init__(self, item):
        """ (Node, object) -> NoneType
        Create a new node storing item, pointing to nothing.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.

    Attributes:
    - first (Node): the first node in the list, or
                    None if the list is empty
    """

    def __init__(self, items):
        """ (LinkedList, list) -> NoneType

        Create Node objects linked together in the order provided in items.
        Set the first node of the list as the first item in items.
        """

        if len(items) == 0:  # No items, and an empty list!
            self.first = None
        else:
            self.first = Node(items[0])
            current_node = self.first
            for item in items[1:]:
                current_node.next = Node(item)
                current_node = current_node.next
    
 
    def is_empty(self):
        """ (LinkedList) -> bool
        Return True if this list is empty.
        """
        return self.first is None


    def __len__(self):
        """ (LinkedList) -> int
        Return the number of elements in this list.
        """
        curr = self.first
        size = 0
        while curr is not None:
            size = size + 1
            curr = curr.next
        return size


    def __getitem__(self, index):
        """ (LinkedList, int) -> object

        Return the item at position index in this list.
        Raise IndexError if index is >= the length of self.
        """
        #if len(self) <= index:
        #    raise IndexError

        curr = self.first
        # Iterate to (index)-th node
        try:
            for i in range(index):
                curr = curr.next
            return curr.item
        
        except AttributeError:
            raise IndexError


    def remove(self, index):
        """ (LinkedList, int) -> NoneType

        Remove node at position index.
        Raise IndexError if index is >= the length of self.
        """
        if len(self) <= index:
            raise IndexError

        if index == 0:
            self.first = self.first.next
        else:
            # Iterate to (index-1)-th node
            curr = self.first
            for i in range(index - 1):
                curr = curr.next

            # Update link to skip over i-th node
            curr.next = curr.next.next

            
    def removeB(self, index):
        """ (LinkedList, int) -> NoneType

        Remove node at position index.
        Raise IndexError if index is >= the length of self.
        """
        
        try:
            curr = self.first
            if index == 0:
                self.first = self.first.next
            
            else:
            

                for i in range(index - 1):
                    curr = curr.next
                
                curr.next = curr.next.next
            
        except AttributeError:
            raise IndexError
        

    def insert(self, index, item):
        """ (LinkedList, int, object) -> NoneType

        Insert a new node containing item at position index.
        Raise IndexError if index is > the length of self.
        Note that adding to the end of a linked list is okay.
        """
        if index > len(self):
            raise IndexError

        # Create new node
        new_node = Node(item)

        if index == 0:
            new_node.next = self.first
            self.first = new_node
        else:
            # Iterate to (index-1)-th node
            curr = self.first
            for i in range(index - 1):
                curr = curr.next

            # Update links to insert new node
            new_node.next = curr.next
            curr.next = new_node
            

    def insertB(self, index, item):
        """ (LinkedList, int, object) -> NoneType

        Insert a new node containing item at position index.
        Raise IndexError if index is > the length of self.
        Note that adding to the end of a linked list is okay.
        """

        try:
        # Create new node
            curr = self.first
            new_node = Node(item)

            if index == 0:
                new_node.next = self.first
                self.first = new_node
            else:
                # Iterate to (index-1)-th node

                for i in range(index - 1):
                    curr = curr.next
    
                # Update links to insert new node
                new_node.next = curr.next
                curr.next = new_node
        except AttributeError:
            raise IndexError


    def __contains__(self, item):
        """ (LinkedList, object) -> bool

        Return True if item is in this list.
        >>> linked = LinkedList([1, 2, 3])
        >>> 1 in linked
        True
        >>> 4 in linked
        False
        """
        
        curr = self.first
        
        while curr is not None:
            
            if item == curr.item:
                return True
            else:
                curr = curr.next
            
        else:
            return False


    def __str__(self):
        """ (LinkedList) -> str

        Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.
        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        """
        string_to_return = "["
        curr = self.first
        
        while curr is not None:
            if curr.next is not None:
                string_to_return += str(curr.item) + " -> " 
            else:
                string_to_return += str(curr.item)
            curr = curr.next
            
        return string_to_return + "]"
    

    def __setitem__(self, index, new_item):
        """ (LinkedList, int, object) -> NoneType

        Store item at position index in self.
        Raise IndexError if index is >= the length of self.
        >>> lst = LinkedList([1, 2, 3])
        >>> lst[1] = 100
        >>> str(lst)
        '[1 -> 100 -> 3]'
        """
        
        try:
            curr = self.first
            
            for i in range(index):
                curr = curr.next
            
            curr.item = new_item
            
        except AttributeError:
            raise IndexError
        

    def delete_item(self, item):
        """ (LinkedList, object) -> NoneType

        Remove the FIRST occurrence of item in self.
        Do nothing if self does not contain item.
        >>> lst = LinkedList([1, 2, 3])
        >>> lst.delete_item(2)
        >>> str(lst)
        '[1 -> 3]'
        """
        
        curr = self.first
        
        if self.first.item == item:
            self.first = self.first.next
            
        else:
            while curr is not None:
                next_ = curr.next
                if next_.item == item:
                    curr.next = curr.next.next
                else:
                    curr = curr.next

     
    def map(self, f):
        """ (LinkedList, function) -> LinkedList

        Return a new LinkedList whose nodes store items that are obtained by
        applying f to each item in this linked list.
        Note: does not change this linked list.

        >>> list = LinkedList(['Hello', 'Goodbye'])
        >>> str(list.map(upper))
        ['HELLO' -> 'GOODBYE']
        >>> str(list.map(len))
        [5 -> 7]
        """
        llist = LinkedList([])
        first_node = Node(f(self.first.item))
        llist.first = first_node
        
        ll_curr = llist.first
        curr = self.first
        
        while curr is not None:
            new_node = Node(f(curr.item))
            new_node.next = ll_curr.next
            ll_curr = new_node
            ll_curr = ll_curr.next
            curr = curr.next
            
        return llist
    

    def pop(self):
        
        try:
            curr = self.first
            
            if self.first.next is None:
                thing_to_pop = self.first.item
                self.first = self.first.next
                
                return thing_to_pop
            
            else:
                while curr.next.next is not None:
                    curr = curr.next
                
                    thing_to_pop = curr.next
                    curr.next = curr.next.next
                    return thing_to_pop.item 
            
        except AttributeError:
            raise IndexError
        

    def append(self,item):
        new_node = Node(item)
        
        if self.first == None:
            self.first = new_node
            
        
        else:
            curr = self.first
            while curr.next is not None:
                curr = curr.next
                
            curr.next = new_node


    def delete_range(self,low,high):
        
        try:
            curr = self.first
            
            if low == 0:
                for idx in range(high):
                    curr = curr.next
                self.first = curr
                
            else:
                low_node = self.first
                high_node = self.first
                for idx in range(low):
                    low_node = low_node.next
                
                for idx in range(high):
                    high_node = high_node.next
                
                low_node.next = high_node
                print(low_node.item)
                print(high_node.item)
                
        except AttributeError:
            raise IndexError
        
        
    def __eq__(self,other):
        
        try:
            curr_self = self.first
            curr_other = other.first

            
            while (curr_self is not None) and (curr_other is not None):
                if not (curr_self.item == curr_other.item):
                    return False
                
                else:
                    curr_self = curr_self.next;
                    curr_other = curr_other.next;
                    
            
            #if both lists are totally iterated through without returning 
            #false or throwing an exception, then the lists are equal
            return (curr_self is None) and (curr_other is None)
                    
        except AttributeError:
            return False
        
