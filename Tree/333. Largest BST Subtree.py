# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
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

        res = [0]
        self.dfs(root, res)
        return res[0]

    def dfs(self, root, res):
        # return left number
        if not root:
            return True, 0, float('INFINITY'), -float('INFINITY')

        l_bst, l_nodes, l_min, l_max = self.dfs(root.left, res)
        r_bst, r_nodes, r_min, r_max = self.dfs(root.right, res)
        sum_nodes = l_nodes + r_nodes + 1
        root_bst = False
        if l_max < root.val <= r_min:
            root_bst = l_bst and r_bst
        if root_bst:
            prev_max = res.pop()
            res.append(max(prev_max, sum_nodes))
        return root_bst, sum_nodes, min(l_min, r_min, root.val), max(r_max, l_max, root.val)
