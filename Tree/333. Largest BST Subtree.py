# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
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

        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return 0, float('INFINITY'), -float('INFINITY')

        l_nodes, l_min, l_max = self.dfs(root.left)
        r_nodes, r_min, r_max = self.dfs(root.right)
        if l_max < root.val < r_min:
            return l_nodes + r_nodes + 1, min(l_min, root.val), max(root.val, r_max)
        return max(l_nodes, r_nodes), -float('inf'), float('inf')
