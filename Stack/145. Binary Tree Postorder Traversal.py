# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # [(left), (right), root]
        #    root
        #    /  \
        #   l     r
        #  / \   / \
        # ll lr rl  rr
        # node.left -> node.right -> node.val
        #
        res = []
        self.postorderTraversal_subtree(root, res)
        return res

    def postorderTraversal_subtree(self, root, res):
        if not root:
            return True
        if self.postorderTraversal_subtree(root.left, res) and self.postorderTraversal_subtree(root.right, res):
            res.append(root.val)
            return True
        return False
