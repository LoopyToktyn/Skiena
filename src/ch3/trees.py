from src.util_classes import TreeNode

"""
3-12. [3] The maximum depth of a binary tree is the number of nodes on the path
from the root down to the most distant leaf node. Give an O(n) algorithm to
find the maximum depth of a binary tree with n nodes.
"""


def depth(root: TreeNode) -> int:
    if root is None:
        return 0
    return max(depth(root.left),depth(root.right)) + 1


tree = TreeNode.build_random_tree(10)
print(tree)
print(f"Depth: {depth(tree)}")