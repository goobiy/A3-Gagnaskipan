#
# BST - Trees (Binary Search Trees)
# Your name:
#  - <Add your name here>
#
from interface.binary_search_tree_abc import Pair, IBinarySearchTree


class BinarySearchTree(IBinarySearchTree):
    """
    A class for a binary search tree, storing (key, value) pairs.
    Only unique key values are allowed.
    IMPORTANT:
        - You are not allowed to change the interface of the existing class methods (public/private),
          nor the _Note class. Doing so will result in non-graded submission.
          However, feel free to add other helper methods as you see fit.
    """

    # --------------------------------------------------------------------------------------
    # Private helper methods and classes (hint: once implemented try to reuse them as
    # much as possible in your public methods).
    # --------------------------------------------------------------------------------------

    class _Node:
        """

        pairsode class for creating the nodes in the tree (Do not change!).
        """
        def __init__(self, parent, left, right, pair: Pair):
            self.parent = parent
            self.left = left
            self.right = right
            self.pair = pair

    def _representation(self, node: _Node) -> str:
        if node is None:
            return "-"
        l = self._representation(node.left)
        r = self._representation(node.right)
        return '(' + str(node.pair) + ' ' + l + ' ' + r + ')'

    # The __iter__ and __reversed__ will be used to test the _first/_last/_before/_after methods.
    def __iter__(self):
        node = self._first()
        while node is not None:
            yield node.pair
            node = self._after(node)

    def __reversed__(self):
        node = self._last()
        while node is not None:
            yield node.pair
            node = self._before(node)


    def _first(self) -> _Node | None:
        """
        In a non-empty tree, returns the minimum key node (first in an inorder traversal), otherwise None.
        """
        
        curr = self._root
        if curr is None:
            return None
        
        while curr.left is not None:
            curr = curr.left
        return curr
    

    def _last(self) -> _Node | None:
        """
        In a non-empty tree, returns the maximum key node (last in an inorder traversal), otherwise None.
        """
        
        curr = self._root
        if curr is None:
            return None
        
        while curr.right is not None:
            curr = curr.right
        return curr
    

    def _before(self, node: _Node) -> _Node | None:
        """
        Returns the in-order predecessor of node, or None if it does not exist.
        """
        if node is self._first():
            return None
    
        curr = node

        if curr.left is not None:
            curr = curr.left

            while curr.right is not None:
                curr = curr.right
            return curr


        while curr.parent.pair.key > curr.pair.key:
            curr = curr.parent

        return curr.parent


    def _after(self, node: _Node) -> _Node | None:
        """
        Returns the in-order successor of node, or None if it does not exist.
        """
        if node is self._last():
            return None
    
        curr = node

        if curr.right is not None:
            curr = curr.right

            while curr.left is not None:
                curr = curr.left
            return curr


        while curr.parent.pair.key < curr.pair.key:
            curr = curr.parent

        return curr.parent

        
    # --------------------------------------------------------------------------------------
    # Public methods, implementing the abstract-base-class interface.
    # --------------------------------------------------------------------------------------

    def __init__(self):
        # This is the only member variable you need. Do not change the constructor.
        self._root: None | BinarySearchTree._Node = None

    def __str__(self) -> str:
        """
        Returns a string representation of the tree.
        """
        return self._representation(self._root)

    def insert_key(self, key: object) -> bool:  # Method is non-essential, but added for testing convenience.
        """
        Insert (key, None) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, None) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        return self.insert(Pair(key, None))

    def keys(self) -> list[object]: # Method is non-essential, but added for testing convenience.
        """
        Returns a list of all the keys in the tree, in an increasing order.
        """
        return [pair.key for pair in self.pairs()]

    def insert(self, pair: Pair) -> bool:
        """
        Insert (key, value) element at the appropriate location in the tree if key does not already exist;
        if the key already exists in the tree, then override with the new (key, value) pair.
        Returns True is a new element was inserted, otherwise False (was updated).
        """
        
        curr: BinarySearchTree._Node = self._root
        if curr is None:
            new_node = self._Node(None,None,None,pair)
            self._root = new_node
            return True

        while True:

            if pair.key == curr.pair.key:
                curr.pair.value = pair.value
                return False
            
            elif pair.key > curr.pair.key:
                if curr.right is None:
                    new_node = self._Node(curr,None,None,pair)
                    curr.right = new_node
                    return True
                curr: BinarySearchTree._Node = curr.right

            
            else:   
                if curr.left is None:
                    new_node = self._Node(curr,None,None,pair)
                    curr.left = new_node
                    return True
                curr: BinarySearchTree._Node = curr.left


    def is_empty(self) -> bool:
        """
        Returns True if the tree is empty, False otherwise.
        """
        return self._root is None
    

    def is_in(self, key: object) -> bool:
        """
        Returns True if an element with key is in the tree, otherwise False.
        """
        curr: BinarySearchTree._Node = self._root
        if curr is None:
            return False

        while True:

            # if key == curr.pair.key:
            #     curr.pair.value = pair.value
            #     return False
            
            if key > curr.pair.key:
                if curr.pair.key == key:
                    return True
                if curr.right is None:
                    return False
                curr: BinarySearchTree._Node = curr.right

            
            else:   
                if curr.pair.key == key:
                    return True
                if curr.left is None:
                    return False
                curr: BinarySearchTree._Node = curr.left


    def get(self, key: object) -> object:
        """
        Returns the value of the element with the given key, or None if the key does not exist.
        """

        curr = self._root

        while curr is not None:
            if curr.pair.key == key:
                return curr.pair.value
            
            if key > curr.pair.key:
                curr = curr.right

            else:
                curr = curr.left

        return None
    

    def pairs(self) -> list[Pair]:
        """
        Returns a list of all the (key, value) pairs in the tree, in an increasing order.
        """

        pairs_list = []
        for pair in self:
            pairs_list.append(pair)
        return pairs_list


    def clear(self):
        """
        Removes all elements from the tree (tree becomes empty).
        """
        self._root = None
    
    def delete_node(self, node: BinarySearchTree._Node) -> bool:



        # Two children
        if node.left is not None and node.right is not None:
            predecessor = self._before(node)
            node.pair = predecessor.pair
            self.delete_node(predecessor)

        # No children or one child
        else:
            # Assigning child to the left node or the right node
            child = node.left if node.left is not None else node.right
            
            # If the node is the root
            if node.parent is None:
                self._root = child
                if child is not None:
                    child.parent = None
            
            # Not the root
            else:
                # Point the parent to the new child
                if node.parent.left is node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            
            if child is not None:
                child.parent = node.parent


    def delete(self, key: object) -> bool:
        """
        Deletes the element with key, if exists.
        Returns True if the element was deleted (existed), otherwise False (does not exist).
        """

        curr = self._root

        while curr is not None and curr.pair.key != key:
            curr = curr.right if key > curr.pair.key else curr.left

        if curr is None:
            return False

        self.delete_node(curr)
        return True