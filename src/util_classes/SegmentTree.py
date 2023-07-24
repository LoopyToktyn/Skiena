from __future__ import annotations
from typing import TypeVar, List, Callable
from math import log2,ceil

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
        self.size = 2**ceil(log2(len(value_list))) # Need to pretend this is a full complete tree
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
    
    def compare(self,v1,v2) -> T:
        if v1 is None and v2 is None:
            raise ValueError("Cannot compare two Nones!")
        if v1 is None:
            return v2
        if v2 is None:
            return v1
        return self.func(v1,v2)

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
                parent = TreeNode(self.compare(left.val,right.val),left,right)
                parents.append(parent)
            else: # No right child means we just use the value of the left child
                parent = TreeNode(left.val,left,right)
                parents.append(parent)
        
        return self.init_balanced_helper(parents)
    
    
    """
           4
       3       4
     1   3   4   n
    0 1 2 3 4 n n n

    1,2
    4  0,7         partial inclusive, return func(left,right) 
      3  0,3       partial inclusive, return func(left,right)
        1  0,1     partial inclusive, return func(left,right)
          1  1,1   within start-end, return
        3  2,3     partial inclusive, return func(left,right)
          2  2,2   within start-end, return
      4  4,7       non-inclusive, do nothing
    """
    def query(self, start: int, end: int) -> T:
        return self.query_helper(self.root, start, end, 1, self.size)

    def query_helper(self,node,start,end,node_start,node_end) -> T:
        # Case 1, this node in inclusive of query range and can be returned
        inclusive = start <= node_start and end >= node_end
        if inclusive:
            return node.val
        
        # Case 2, this node includes nothing in query range
        not_inclusive = end < node_start or start > node_end
        if not_inclusive:
            return None

        # Case 3, this node partially included in query range, check both children. Ignore None-children
        mid = (node_start + node_end) // 2
        left = None
        right = None
        if node.left:
            left  = self.query_helper(node.left , start, end, node_start, mid     )
        if node.right:
            right = self.query_helper(node.right, start, end, mid + 1   , node_end)
        
        return self.compare(left,right)
