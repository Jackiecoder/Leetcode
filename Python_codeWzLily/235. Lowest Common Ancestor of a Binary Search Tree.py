# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # find the node.val between p and q
        # def find_lca
        #   input: node, p, q
        #   output:
        #   if q.val < node.val < p.val -> return node
        #   else if  node > p, node > q -> return find_lca(node.left)
        #   else: return find_lca(node.right)
        # Time O(h), h -> depth of the tree
        # space O(1)

        return self.find_lca(root, p, q)

    def find_lca(self, node, p, q):
        if not node:
            return None
        if node.val > p.val and node.val > q.val:
            return self.find_lca(node.left, p, q)
        elif node.val < p.val and node.val < q.val:
            return self.find_lca(node.right, p, q)
        else:
            return node
