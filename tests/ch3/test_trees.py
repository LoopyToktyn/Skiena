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
def test_find_two_nerds1(): # 2,1
    root = t1
    root.left = t2
    assert find_nerds_v3(root) == (t2,t1)

def test_find_two_nerds2(): # 1,3,2
    root = t3
    root.left = t1
    root.right = t2
    assert find_nerds_v3(root) == (t3,t2)

def test_find_two_nerds3(): # 3,2,1
    root = t2
    root.left = t3
    root.right = t1
    assert find_nerds_v3(root) == (t3,t1)

def test_find_two_nerds4(): # 1,4,3,2
    root = t4
    root.left = t1
    root.right = t3
    root.right.right = t2
    assert find_nerds_v3(root) == (t4,t2)

def test_find_two_nerds5(): # 4,2,3,1
    root = t3
    root.left = t2
    root.left.left = t4
    root.right = t1
    assert find_nerds_v3(root) == (t4,t1)

def test_find_two_nerds6(): # 1,2,5,4,3,6
    root = t4
    root.left = t2
    root.left.right = t5
    root.left.left = t1
    root.right = t6
    root.right.left = t3
    assert find_nerds_v3(root) == (t5,t3)


def test_is_balanced1():
    root = t4
    root.left = t2
    root.left.right = t5
    root.left.left = t1
    root.right = t6
    root.right.left = t3
    assert is_balanced(root)

def test_is_balanced2():
    root = t1
    root.left = t2
    root.left.left = t3
    root.left.right = t7
    root.left.left.left = t4
    root.left.left.right = t5
    root.right = t6
    assert not is_balanced(root)

def test_is_balanced3():
    root = t1
    root.left = t2
    root.left.right = t5
    root.left.left = t4
    root.left.left.left = t8
    root.right = t3
    root.right.left = t6
    assert is_balanced(root)