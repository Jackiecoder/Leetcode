# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder deserialize
        # use a stack to do DFS
        # e.g.
        # stack = [6]
        # node = 5
        # res = [1, 2, 3, 4]
        # Time O(n), space O(n)
        if not root:
            return
        prev = None
        stack = [root]
        while stack:
            node = stack.pop()
            if prev:
                prev.right = node
                prev.left = None
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node
