# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # find maximum sum that pass the node
        #    41
        # 9.     42
        # .    15.   7
        # we can start from the leaf node to the root
        # -> backtracking to solve it.
        # we must choose from (node.val + left + right) and (node.val + max(left, right)) + sth above it
        # time O(n), space O(1)
        if not root:
            return -2147483648
        max_sum = [-float('INFINITY')]
        self.max_sum_wz_node(root, max_sum)
        return max_sum[0]

    def max_sum_wz_node(self, node, max_sum):
        # if call this function, means node is valid -> not None
        if not node.left and not node.right:
            if node.val > max_sum[0]:
                max_sum.pop()
                max_sum.append(node.val)
            return node.val
        left_sum, right_sum = 0, 0
        if node.left:
            left_sum = max(0, self.max_sum_wz_node(node.left, max_sum))
        if node.right:
            right_sum = max(0, self.max_sum_wz_node(node.right, max_sum))
        node_as_root = node.val + left_sum + right_sum
        if max_sum[0] < node_as_root:
            max_sum.pop()
            max_sum.append(node_as_root)
        return node.val + max(left_sum, right_sum)

    def maxPathSum_wz_global(self, root: TreeNode) -> int:
        # find maximum sum that pass the node
        #    41
        # 9.     42
        # .    15.   7
        # we can start from the leaf node to the root
        # -> backtracking to solve it.
        # we must choose from (node.val + left + right) and (node.val + max(left, right)) + sth above it
        # time O(n), space O(1)
        if not root:
            return -2147483648
        self.max_sum = -float('INFINITY')
        self.max_sum_wz_node_global(root)
        return self.max_sum

    def max_sum_wz_node_global(self, node):
        # if call this function, means node is valid -> not None
        if not node.left and not node.right:
            self.max_sum = max(self.max_sum, node.val)
            return node.val
        left_sum, right_sum = 0, 0
        if node.left:
            left_sum = max(0, self.max_sum_wz_node_global(node.left))
        if node.right:
            right_sum = max(0, self.max_sum_wz_node_global(node.right))
        node_as_root = node.val + left_sum + right_sum
        self.max_sum = max(self.max_sum, node_as_root)
        return node.val + max(left_sum, right_sum)
