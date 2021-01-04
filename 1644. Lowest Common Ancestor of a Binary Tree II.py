# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node, found = self.dfs(root, p, q, 0)
        return node if found == 2 else None

    def dfs(self, node, p, q, found):
        if not node:
            return None, 0
        l_node, l_found = self.dfs(node.left, p, q, found)
        r_node, r_found = self.dfs(node.right, p, q, found)
        if l_found == 2:
            return l_node, l_found
        if r_found == 2:
            return r_node, r_found
        found = 1 if node is p or node is q else 0
        found += l_found + r_found
        return node, found
