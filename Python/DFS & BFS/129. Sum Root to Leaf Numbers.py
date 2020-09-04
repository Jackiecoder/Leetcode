# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # dfs
        # find all number and sum
        # Time O(n), space O(1)
        if not root:
            return 0
        res = []
        self.dfs(root, str(root.val), res)
        return sum(res)

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            res.append(int(path))
            return
        if root.left:
            self.dfs(root.left, path + str(root.left.val), res)
        if root.right:
            self.dfs(root.right, path + str(root.right.val), res)
