# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # loop ->
        # min -> record the cloest number
        # while (node is valid)
        #   node.val compare the target
        #   if node.val > target -> move to node.left
        #   else if node.val == target -> return this value
        #   else -> move to node.right
        # return
        # Time O(h), space O(1)
        res = root.val
        while root:
            if abs(root.val - target) < abs(res - target):
                res = root.val
            if root.val == target:
                return int(target)
            elif root.val > target:
                root = root.left
            else:
                root = root.right
        return res
