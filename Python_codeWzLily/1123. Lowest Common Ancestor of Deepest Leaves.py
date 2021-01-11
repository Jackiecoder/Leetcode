# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        # return node and its level
        # if level is deeper than previous, then use this lca
        # there will be several cases:
        #   1. leaf node:
        #       l_node, r_node are None, and return this leaf node, and its level
        #   2. one child:
        #       return its node, and the level of its child
        #   3. two child:
        #       if l_lvl == r_lvl, return node, l_lvl
        #       else:
        #           return the child with deeper node
        # Time O(n), space O(1)
        lca, _ = self.dfs(root, 0)
        return lca

    def dfs(self, node, lvl):
        if not node:
            return node, lvl
        l_node, l_lvl = self.dfs(node.left, lvl + 1)
        r_node, r_lvl = self.dfs(node.right, lvl + 1)
        if l_lvl == r_lvl:
            return node, l_lvl
        elif l_lvl > r_lvl:
            return l_node, l_lvl
        else:
            return r_node, r_lvl
