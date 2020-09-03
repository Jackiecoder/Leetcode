# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # when this function called -> t1, t2 must have one valid
        if not t1 and not t2:
            return None
        value = 0
        t1_left, t1_right, t2_left, t2_right = None, None, None, None
        if t1:
            value += t1.val
            t1_left = t1.left
            t1_right = t1.right
        if t2:
            value += t2.val
            t2_left = t2.left
            t2_right = t2.right
        root = TreeNode(value)
        root.left = self.mergeTrees(t1_left, t2_left)
        root.right = self.mergeTrees(t1_right, t2_right)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # when this function called -> t1, t2 must have one valid
        if not t1 and not t2:
            return None
        root = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        root.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        root.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return root
