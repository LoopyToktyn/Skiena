from __future__ import annotations
from typing import TypeVar, List, Callable

T = TypeVar('T')

class TreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: TreeNode) -> bool:
        if not isinstance(other,TreeNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right
    
    def __str__(self) -> str:
        res = repr(self.val) + " "
        if self.left:
            res += repr(self.left.val) + " "
        if self.right:
            res += repr(self.right.val) + " "
        return res

class SegmentTree:
    def __init__(self, value_list: List[T], func: Callable[[T,T], T]) -> None:
        self.func = func
        self.root: TreeNode = self.init_balanced(value_list)
    
    def __eq__(self, other: SegmentTree) -> bool:
        if not isinstance(other,SegmentTree):
            return False
        return self.root == other.root
    
    def __str__(self) -> str:
        return repr(self.root)

    def init_balanced(self, value_list: List[T]) -> TreeNode:
        # init values as TreeNodes
        nodes = list(map(TreeNode,value_list))
        return self.init_balanced_helper(nodes)

    def init_balanced_helper(self, nodes: List[TreeNode]) -> TreeNode:
        if len(nodes) == 1:
            return nodes[0]

        parents = []

        # Let's make sure we've got an even length list for the following for loop
        if len(nodes) % 2 != 0:
            nodes.append(None)
        
        # Apply the function to each pair of children to create a list of parent nodes
        for i in range(0,len(nodes),2):
            left = nodes[i]
            right = nodes[i+1]
            if left and right:
                parent = TreeNode(self.func(left.val,right.val),left,right)
                parents.append(parent)
            else: # No right child means we just use the value of the left child
                parent = TreeNode(left.val,left,right)
                parents.append(parent)
        
        return self.init_balanced_helper(parents)
    
    def query(self, start: int, end: int):
        
        pass