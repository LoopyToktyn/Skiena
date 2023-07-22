import sys
sys.path.insert(0, r'F:\ws-py3\Skiena')
from src.util_classes import TreeNode
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

print(TreeNode.init_balanced([1,2,3,4,5]))