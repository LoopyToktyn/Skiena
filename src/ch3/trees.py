from src.util_classes import TreeNode
from typing import List

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

# Nope, that didn't work either. Consider the list 5,6,1,2,3,4. 5 might check out, 6 wouldn't, and now we might be looking at a sort problem of nlgn
# New new idea. What if for every node, we check it against its parent AND children? Might not work, recursion would fall apart when looking at a 
# child that assumes its parent is a good person. Each node has to look its entire branch maybe? That would be nlgn though, not n. HMMM.

# I think the key is that I need to specifically be looking for just two. Looking for all is definitely not an O(n) problem. Let's go back
# to my last attempt. If I do a findmin on the list, O(n), I can do two sets of ops. First I loop and look for anything greater than min
# at the beginning of the list. Once I get to min, then I just need to check that every element is less than the next element, ignoring last element

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



# Below are some naive attempts. Finding one nerd is cool but kills the search and is wrong because it assumes the parent
# is the invalid node when it could be the child. Consider the tree 5, 3l, 6r where find_one_nerd would return None
# find_nerds attempts to find all misplaced nodes but has the same problems in approach as find_one_nerd
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
    



tree = TreeNode.build_random_tree(10)
print(tree)
print(f"Depth: {depth(tree)}")