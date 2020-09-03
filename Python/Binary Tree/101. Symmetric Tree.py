# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # create recursion function:
        #   root1, root2
        #   if root1 and root2 both None -> True
        #   if only one of those root is None -> False
        #   if root1.val == root2.ve
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
