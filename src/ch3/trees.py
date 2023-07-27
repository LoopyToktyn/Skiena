import sys
sys.path.insert(0, r'F:\ws-py3\Skiena')
from src.util_classes.BinarySearchTree import TreeNode
from src.util_classes.SegmentTree import TreeNode as SegTreeNode
from src.util_classes.CountSmallerTree import CountTreeNode
from src.util_classes.BinaryIndexTree import BinaryIndexTree
from typing import List
from collections import deque
  

"""
3-12. [3] The maximum depth of a binary tree is the number of nodes on the path
from the root down to the most distant leaf node. Give an O(n) algorithm to
find the maximum depth of a binary tree with n nodes.
"""
def depth(root: TreeNode) -> int:
    if root is None:
        return 0
    return max(depth(root.left),depth(root.right)) + 1

"""
3-13. [5] Two elements of a binary search tree have been swapped by mistake. Give
an O(n) algorithm to identify these two elements so they can be swapped back.
"""
def find_nerds(root: TreeNode) -> List[TreeNode]:
    if root is None: 
        return []
    
    if root.left and root.val < root.left.val or root.right and root.val > root.right.val:
        return [root.val] + find_nerds(root.left) + find_nerds(root.right)

    return find_nerds(root.left) + find_nerds(root.right)


def find_one_nerd(root: TreeNode) -> TreeNode:
    #  If we've hit a None node, we've hit a leaf
    if root is None:
        return None

    # Check if this node is bad. If so, we've found 'em!
    if root.left and root.val < root.left.val or root.right and root.val > root.right.val:
        return root
    
    # If all clear, keep searching
    left_result = find_one_nerd(root.left)
    right_result = find_one_nerd(root.right)
    if left_result:
        return left_result
    if right_result:
        return right_result
    # if neither
    return None

# Above are some naive attempts. Finding one nerd is cool but kills the search and is wrong because it assumes the parent
# is the invalid node when it could be the child. Consider the tree 5, 3l, 6r where find_one_nerd would return None
# find_nerds attempts to find all misplaced nodes but has the same problems in approach as find_one_nerd

# New idea, let's traverse the tree left to right to create what should be a sorted list. 
# Then we traverse the list and validate that each element is less than the previous or greater than the next (special care for ends of list)
def find_nerds_v2(root: TreeNode) -> List[TreeNode]:
    all_nodes = create_list_left_right(root)
    if len(all_nodes) == 0: 
        return None
    result = []
    min = None
    for node in all_nodes:
        if min is None:
            min = node.val
            continue
        if node.val < min:
            min = node.val
    
    i = 0
    current_node = all_nodes[i]
    while current_node.val > min and i < len(all_nodes):
        result.append(current_node)
        i += 1
        current_node = all_nodes[i]

    for j in range(i+1,len(all_nodes)-1):
        if all_nodes[j].val > all_nodes[j+1].val:
            result.append(all_nodes[j])

    if len(result) > 2:
        print(result)
        raise ValueError("Houston, we've got more than two problems here")
    
    return result
    

def create_list_left_right(root: TreeNode) -> List[TreeNode]:
    if root is None:
        return []
    return create_list_left_right(root.left) + [root] + create_list_left_right(root.right)

# Nope, that didn't work either. Consider the list 5,6,1,2,3,4. 5 might check out, 6 wouldn't, and now we might be looking at a sort problem of nlgn
# New new idea. What if for every node, we check it against its parent AND children? Might not work, recursion would fall apart when looking at a 
# child that assumes its parent is a good person. Each node has to look its entire branch maybe? That would be nlgn though, not n. HMMM.

# I think the key is that I need to specifically be looking for just two. Looking for all is definitely not an O(n) problem. Let's go back
# to my last attempt. If I do a findmin on the list, O(n), I can do two sets of ops. First I loop and look for anything greater than min
# at the beginning of the list. Once I get to min, then I just need to check that every element is less than the next element, ignoring last element


# Going back and finishing that idea was still fruitless. Something I didn't consider is that 5,6,1,2,3,4 is an invalid list for SWAP 2. That is indeed
# a key requirement of this problem. Let's build a set of example lists that are VALID, meaning only 2 nodes are out of position. In that last list, the whole
# dang thing is a problem.

# 2,1 (swap 1 and 2)
# 1,3,2 (swap 2 and 3)
# 3,2,1 (swap 1 and 3)
# 1,4,3,2 (4 & 2)
# 4,2,3,1 (1 & 4)
# 1,2,5,4,3,6 (3 & 5)

# Given this set, let's find the pattern. The two nodes we're looking for appear to always be:
# 1) the first node greater than the next node
# 2) the last node less than the previous node (the first node less than will be the one immediately after step 1, but we could find another later in the list)
# If this holds, then we were off to a good start by traversing and creating a list. We fell off track with the algorithm that then stepped through that list.
# Let's try again!

def find_nerds_v3(root: TreeNode) -> tuple[TreeNode,TreeNode]:
    nodes = create_list_left_right(root)
    greater = None
    lesser = None
    for i in range(len(nodes)):
        if i < len(nodes) and greater is None and nodes[i].val > nodes[i+1].val:
            greater = nodes[i]
        if i > 0 and nodes[i].val < nodes[i-1].val:
            lesser = nodes[i]
    return (greater,lesser)


"""
3-17. [5] Give an O(n) algorithm that determines whether a given n-node binary tree
is height-balanced (see Problem 3-15).
"""

def is_balanced(root: TreeNode) -> bool:
    max_min = is_balanced_helper(root)
    return max_min[1] - max_min[0] < 2

def is_balanced_helper(root: TreeNode) -> tuple[int,int]:
    if root is None:
        return 0,0
    left_min, left_max = is_balanced_helper(root.left)
    right_min, right_max = is_balanced_helper(root.right)

    return min(left_min,right_min) + 1, max(left_max,right_max) + 1


# Above approach was naive and misunderstood the definition of height-balanced. See test 3 for an example of where that algo gives the wrong answer
# New approach, we keep a truthiness of each subtree as well as keep track of the max depth so far. Short circuit if we find a boner.

def is_balanced_v2(root: TreeNode) -> bool:
    balanced,height = is_balanced_helper_v2(root)
    return balanced

def is_balanced_helper_v2(root: TreeNode) -> tuple[bool,int]:
    if root is None:
        return True,0
    
    left_balanced, left_height = is_balanced_helper_v2(root.left)
    right_balanced, right_height = is_balanced_helper_v2(root.right)

    if not left_balanced or not right_balanced:
        return False,0 # value doesn't matter here, don't bother calculating anything

    return abs(left_height - right_height) < 2, max(left_height,right_height) + 1



"""
3-24. [5] An array A is called k-unique if it does not contain a pair of duplicate
elements within k positions of each other, that is, there is no i and j such that
A[i] = A[j] and |j - i| ≤ k. Design a worst-case O(n log k) algorithm to test if
A is k-unique.
"""

# I'm gonna need to do some additional work to prep for this one. We're gonna need
# to build a balanced tree and have the ability to insert and delete items from 
# this tree while keeping it balanced. (We gonna do this manual, not use libs)

# Once we've got our ability to make a tree, we're gonna maintain a window of size k
# and step through the array. If at any time we try to add something to the window
# and that window already contains the element, we'll return false.

def is_k_unique(arr: List, k: int) -> bool:
    bbst = TreeNode(arr[0])
    window = deque()

    for c in arr:
        if c in bbst:
            return False
        
        bbst.insert_balanced(c)
        window.append(c)
           
        if len(window) > k:
            oldest = window.popleft()
            bbst.delete_balanced(oldest)

    return True

"""
3-25. [5] In the bin-packing problem, we are given n objects, each weighing at most
1 kilogram. Our goal is to find the smallest number of bins that will hold the n
objects, with each bin holding 1 kilogram at most.
    • The best-fit heuristic for bin packing is as follows. Consider the objects
    in the order in which they are given. For each object, place it into the
    partially filled bin with the smallest amount of extra room after the object is 
    inserted. If no such bin exists, start a new bin. Design an algorithm that 
    implements the best-fit heuristic (taking as input the n weights
    w1, w2, ..., wn and outputting the number of bins used) in O(n log n) time.
    • Repeat the above using the worst-fit heuristic, where we put the next
    object into the partially filled bin with the largest amount of extra room
    after the object is inserted.
"""

# Let's define a BinStruct that maintains max_space and a BBST. Nodes values will represent space_remaining (initialized on creation to max_space)
# max_space will be a constant built into a datastructure wrapping the tree
# BinStruct Functions:
#   - findminbin(item) will find the node with the least space remaining that fits the given item
#     - The underlying tree algorithm here would be to first check the MAX of the tree, AKA the bin with the most space available. If this object is too big
#       for that bin, we can short circuit and immediately just add a new bin. From here there are two approaches:
#       - SIMPLE: start at MIN and call successor until n fits O(n)
#       - TRICKY: traverse like you're doing an INSERT. Once you've found the node under which you would insert this value, if it's greater than current_node, 
#                 return current_node's successor, else return its predecessor O(lg n)
#   - addbin(item) will create a new bin, add it to the tree, and initialize the space_remaining based on the size of the item passed in.
#     This will also increment the count.
#   - update(node,item) will take a node and an item and update the remaining space and rebalance the tree

class BinStruct:
    def __init__(self,max_space) -> None:
        self.max_space = max_space
        self.bins = TreeNode(max_space)
        self.count = 1
    def findminbin(self,size):
        pass
    def addbin(self,item) -> None:
        pass
    def update(self,node,item) -> None:
        pass
    def __len__(self) -> int:
        pass

def best_fit(n,max_space) -> int:
    bins = BinStruct(max_space)

    for i in n:
        min_bin = bins.findminbin(i)
        if min_bin is None:
            bins.addbin(i)
        else:
            bins.update(min_bin,i)

    return bins.count




"""
3-26. [5] Suppose that we are given a sequence of n values x1, x2, ..., xn and seek to
quickly answer repeated queries of the form: given i and j, find the smallest
value in xi,...,xj .
(a) Design a data structure that uses O(n2) space and answers queries in O(1)
time.
(b) Design a data structure that uses O(n) space and answers queries in
O(log n) time. For partial credit, your data structure can use O(n log n)
space and have O(log n) query time.

a) We could design an n x n matrix that maintains the smallest value from any i to j
   Initialization of the matrix would take n^2 time, but lookups would be constant time.
   Init would involve storing the smallest value from i to j in each n x n cell such that matrix[i][j] returns the smallest value
   Matrix would really only need to be half full, no need to store values in any matrix[j][i]

b) O(n) space with O(lg n) time screams "tree!". After a big of digging, I have discovered...The Segment Tree!
   Since we don't have to maintain this or deal with insert/delete operations (although we could and I should build that...),
   We can implement this as a regular BST that's balanced at initialization then just store and use this static structure.
"""



"""
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].
"""

# This works as a good average-case but still has a worst case running time of O(n^2) in the event of descending or ascending list
def count_smaller(nums: List[int]) -> List[int]:
    root = CountTreeNode(nums.pop())
    result = [0]
    while nums:
        val = nums.pop()
        result.append(root.insert(val))
    
    result.reverse()
    return result

def count_smaller_v2(nums: List[int]) -> List[int]:
    # Transform all of our values into a positive integer, ignore duplicates
    # Use a hash table/dictionary for lookup
    sorted_nums = sorted(set(nums))
    ranks = {val: i+1 for i,val in enumerate(sorted_nums)}

    # initialize our BIT and result
    bit = BinaryIndexTree(len(nums))
    result = [0] * len(nums)

    # Perform surgery right to left
    for i in reversed(range(len(nums))):
        rank = ranks[nums[i]] # lookup our rank-equivalent value
        result[i] = bit.query(rank-1) # Get sum of all values smaller than current rank and store in result list
        bit.update(rank,1) # Increment affected ranks by 1

    return result


"""
LEET: Given two integer arrays preorder and inorder where preorder is the preorder traversal 
      of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

PRE 2 1 5 0 3 6 4
IN  5 0 1 3 6 2 4
TR  2 1 4 5 3 n n n 0 6

i = n
[0, n, 2n, 2n+1, 2*2n, 2*2n+1, 3*2n, 3*2n+1]
    r  rl  rr    rll   rlr     rrl   rrr
 
 i=0            i=1         i=2
[i, 2i+1, 2i+2, 2i+1, 2i+2, 2i+1, 2i+2]
 r  rl    rr    rll   rlr   rrl   rrr

i = 1
j = 1
r = 1
prepend both PRE and IN arrays with 0 (for easier intuition)
stack = []
while i < len(PRE)
    if PRE[i] != IN[j], then PRE.next is left child
        set result[r] = PRE[i]
        set result pointer to left child (r = r*2)
        add PRE[i] to stack
        i++
        continue
    else if equal, then next will either be a parent we've already traversed or a new right child.
        result[r] = PRE[i]
        if IN[j+1] != stack[-1], then it's a new right child
            r = r*2 + 1
            i++
            j++
        else we go back up to a parent
            parent = stack.pop()
            r = find_index(parent)
            j++


2 1 _ 5 _ _ _ _ 0 _


OOPS, this is supposed to return a treenode not an array. Maybe solution will be more straight forward? Let's see where we get.
PRE 2 1 3 4 0 6
IN  1 3 2 0 4 6
TR  2 1 4 n 3 0 6

PRE 2 1 3 4 6
IN  3 1 2 4 6
TR  2 1 4 3 n n 6

FUNC(PRE,IN) -> node,PRE,IN
    if not PRE:
        return None, PRE, IN
    while len(IN) > len(PRE): # pop parent nodes
        IN = IN[1:]
    node = TreeNode(PRE[0])
    if PRE[0] == IN[0]
        node.left = None
        node.right,pre_r,in_r = FUNC(PRE[1:], IN[1:])
        return node, pre_r, in_r
    else
        node.left,pre_l,in_l = FUNCT(PRE[1:],IN)
        node.right, pre_r, in_r = FUNC(pre_l, in_l)
        return node, pre_r, in_r

PRE 1,2,3
IN  2,1,3
TR  1,2,3
        
"""

### GARBAGE
# def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
#     node, _, _ = build_tree_helper(deque(preorder),deque(inorder))
#     return node

# def build_tree_helper(PRE: deque[int], IN: deque[int], stack: List[int] = []) -> tuple[TreeNode, List[int], List[int]]:
#     if not PRE:
#         return None, PRE, IN, stack
#     if IN[0] == stack[-1]:
#         stack.pop()
#         IN.popleft()
#         return None, PRE, IN, stack
#     node = TreeNode(PRE[0])
#     if PRE[0] == IN[0]:
#         node.left = None
#         node.right,pre_r,in_r = build_tree_helper(PRE[1:], IN[1:],stack)
#         return node, pre_r, in_r, stack
#     else:
#         stack.append(PRE.popleft())
#         node.left,pre_l,in_l = build_tree_helper(PRE,IN,stack)
#         node.right, pre_r, in_r = build_tree_helper(pre_l, in_l,stack)
#         return node, pre_r, in_r, stack

"""
PRE 1,2,3
IN  2,1,3
TR  1,2,3
"""

def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:

    def helper(right_boundary: int = None) -> TreeNode:
        if not inorder or inorder[0] == right_boundary:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        root.left = helper(root_val)
        inorder.remove(root_val)
        root.right = helper(right_boundary)

        return root
    
    return helper()