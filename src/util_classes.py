from __future__ import annotations
from typing import TypeVar, Generic, List
import random

class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next
    def __str__(self):
        next_val = self.next
        return f"ListNode({self.val}, {next_val})"
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next
    



T = TypeVar('T')

class TreeNode(Generic[T]):
    def __init__(self, val: T, parent: TreeNode = None, left: TreeNode = None, right: TreeNode = None ) -> None:
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, val: T) -> None:
        if val < self.val:
            if self.left == None:
                self.left = TreeNode(val,self,None,None)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right == None:
                self.right = TreeNode(val,self,None,None)
            else:
                self.right.insert(val)
        else:
            raise ValueError(f"No duplicates! Self: {self.val} -- Insert: {val}")
        
    def findmin(self) -> TreeNode:
        if self is None: # We probably shouldn't be calling findmin on a None-leaf, but in case we do...
            return None
        if self.left is None:
            return self
        return self.left.findmin()
        
        
    def delete(self, val: T) -> TreeNode:
        # Base
        if self is None:
            return None
        
        # Traverse
        elif self.left and self.val > val:
            self.left = self.left.delete(val)
        elif self.right and self.val < val:
            self.right = self.right.delete(val)
        else:
            # SINK (Single Income No Kids)
            if self.left is None and self.right is None:
                self = None
            # Uno Kiddado
            elif self.left is None:
                self = self.right
            elif self.right is None:
                self = self.left
            # Mucho Kiddado
            else:
                successor = self.right.findmin()
                self.val = successor.val
                self.right = self.right.delete(successor.val)

        return self
        
                    
        
    @staticmethod
    def init_balanced(elements: List) -> ListNode:
        if not elements:
            return None
        elements.sort()
        median = len(elements) // 2
        # 1,2,3,4 -> 2
        # 0,1,2,3 -> e[2] is 2. Median gives us start of upper half when list is even.
        # 1,2,3 -> 1
        # 0,1,2 -> e[1] gives us 1. Perfect median, same # elements before and after
        # 0,1   -> e[1] gives us 1. Upper half as before.

        # 0,1,2 -> e[:1] returns [0], e[1+1:] returns [2]
        # 0,1   -> e[:1] returns [0], e[1+1:] returns []. This is good for us!
        # 0     -> e[:0] returns [] , e[0+1:] returns []. Fabulous. We shouldn't have to handle any special cases or out of bound errors here.

        # I'm not ready to deal with managing the parent relationship for this. Everyone's an orphan today!
        return TreeNode(elements[median], None, TreeNode.init_balanced(elements[:median]),TreeNode.init_balanced(elements[median+1:]))

    @staticmethod
    def build_random_tree(num_nodes: int) -> TreeNode:
        nodes = [i for i in range(num_nodes)]
        random.shuffle(nodes)
        head = TreeNode(nodes[0])
        for node in nodes[1:]:
            head.insert(node)
        return head

    def __str__(self, level=0):
        ret = "  " * level + repr(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other,TreeNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right
    

