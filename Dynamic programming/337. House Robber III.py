# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        node_to_val = {}
        res = self.rob_subtree(root, True, node_to_val)
        return res

    def rob_subtree(self, root, root_can_be_rob, memo):
        if not root:
            return 0
        if (root, root_can_be_rob) in memo:
            return memo[(root, root_can_be_rob)]

        val = self.rob_subtree(root.left, True, memo) + \
            self.rob_subtree(root.right, True, memo)
        if root_can_be_rob:
            # choose rob root or not
            val = max(val, root.val + self.rob_subtree(root.left, False,
                                                       memo) + self.rob_subtree(root.right, False, memo))
        memo[(root, root_can_be_rob)] = val
        return val
