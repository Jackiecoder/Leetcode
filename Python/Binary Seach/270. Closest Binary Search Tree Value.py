# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # node.val > target:
        #   go left
        # node.val < target:
        #   go right
        # equal -> return
        # record the cur_closest
        # time O(h), space O(1)
        if not root:
            return
        cur_closest = root.val
        cur_node = root
        while cur_node:
            # cur_node is always valid
            cur_closest = cur_node.val if abs(
                cur_node.val - target) < abs(cur_closest - target) else cur_closest
            if target < cur_node.val:
                cur_node = cur_node.left
            elif target > cur_node.val:
                cur_node = cur_node.right
            else:
                return cur_node.val
        return cur_closest
