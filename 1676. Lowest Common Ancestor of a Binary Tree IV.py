# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node, found = self.dfs(root, set(nodes), 0, len(nodes))
        return node

    def dfs(self, node, nodes, found, k):
        # return node, found
        if not node:
            return None, 0
        l_node, l_found = self.dfs(node.left, nodes, found, k)
        r_node, r_found = self.dfs(node.right, nodes, found, k)
        if l_found == k:
            return l_node, k
        if r_found == k:
            return r_node, k
        found = 1 if node in nodes else 0
        found += l_found + r_found
        return node, found
