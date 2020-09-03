
# My method:

# if a subtree is a BST  -> all of its subtree have
#     left child < root < right child
# because we need the result of its left and right subtree to judge if it is a BST
#   thus we can use Backtracking
# the requirement of a BST will be
#   1. left is BST
#   2. right is BST
#   3. left node < root < right node
#   4. root.val in range

# e.g.
#
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7

# if valid -> return number of nodes in subtree
#   else -> return -1
# if leaf -> return 1

# Leetcode discussion (best solution)
#   dfs() return 3 arugments,
# number of nodes in this subtree
# the minimum value in this subtree
# the maximum value in this subtree
#
#   The most tracky part is that, when reach the leaf nodes, we need to return  \
# number = 0, min = float('inf'), max = -float('inf').
# Because when we judge if the parent of the leaf nodes are BST, we need maximum of left and minimum of right. and the left nodes should always be assumed as a one node BST. Thus, -inf < root.val < inf is always valid.
# In addition, when any one of child is invaild. r_min = -inf, l_max = inf will make inf < root.val < -inf invalid.
#                       |
#          |---------|     | ---------|

# Definition for a binary tree node.


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = [0]
        self.isValidBST(root, res)
        return res[0]

    def isValidBST(self, root, res):
        # return isvalid, nodes, min, max
        if not root:
            return True, 0, float('inf'), -float('inf')
        l_valid, l_nodes, l_min, l_max = self.isValidBST(root.left, res)
        r_valid, r_nodes, r_min, r_max = self.isValidBST(root.right, res)
        if not l_valid or not r_valid or not l_max < root.val < r_min:
            return False, None, None, None
        # when code arrive here, means this BST must be valid
        total_nodes = l_nodes + r_nodes + 1
        res[:] = [max(total_nodes, res[0])]
        return True, total_nodes, min(l_min, root.val), max(r_max, root.val)
