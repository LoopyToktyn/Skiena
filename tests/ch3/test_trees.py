from src.ch3.trees import *


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)


# Let's find some nerds
def test_find_two_nerds():
    root = TreeNode(5)
    root.left = t3
    root.left.left = t7 # bad node
    root.left.right = t4
    root.right = t1 # bad node
    # root.right.right = t8
    # root.right.left = t6
    assert set(find_nerds_v2(root)) == set([t1,t7])