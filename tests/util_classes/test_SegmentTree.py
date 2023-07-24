from src.util_classes.SegmentTree import *

## [0,1,2,3]
root0123 = TreeNode(3)
root0123.left = TreeNode(1)
root0123.left.left = TreeNode(0)
root0123.left.right = TreeNode(1)
root0123.right = TreeNode(3)
root0123.right.left = TreeNode(2)
root0123.right.right = TreeNode(3)

## [4,nil,nil,nil]
root4nnn = TreeNode(4)
root4nnn.left = TreeNode(4)
root4nnn.left.left = TreeNode(4)
root4nnn.left.right = None
root4nnn.right = None

def test_init1():
    assert SegmentTree([0,1,2,3],max).root == root0123

def test_init2():
    root = TreeNode(4)
    root.left = root0123
    root.right = root4nnn
    assert SegmentTree([0,1,2,3,4],max).root == root



"""
       4
   3       4
 1   3   4   n
0 1 2 3 4 n n n
"""