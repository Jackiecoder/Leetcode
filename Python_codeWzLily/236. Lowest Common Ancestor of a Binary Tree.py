# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #   divide and conquer
        # several conditions:
        #   1. left subtree find p(q), and itself or right subtree find q(p) -> return this node
        #   2. already find two nodes, -> return that node
        # Time O(n), space O(1) / O(n)
        # e.g.
        #   root ->
        #       1. root.left and root.right contain one node
        #       2. root.left contain two
        #       3. root.left contain one, and node is another one

        # method 1
        # node, _ = self.dfs1(root, p, q, 0)
        # return node

        # method 2
        return self.dfs(root, p, q)

    def dfs(self, node, p, q):
        # because this node must exist, so once we find a valid node, we can return this node immediately.
        if not node:
            return None
        if node is p or node is q:
            return node
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        if left and right:
            return node
        if left:
            return left
        if right:
            return right

    def dfs1(self, node, p, q, found):
        if not node:
            return None, 0
        left, left_found = self.dfs(node.left, p, q, found)
        right, right_found = self.dfs(node.right, p, q, found)
        if left_found == 2:
            return left, 2
        if right_found == 2:
            return right, 2
        found = 1 if node is p or node is q else 0
        found += left_found + right_found
        if found == 2:
            return node, found
        return None, found
