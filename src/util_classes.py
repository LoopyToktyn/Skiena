from __future__ import annotations
from typing import TypeVar, Generic
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
    

