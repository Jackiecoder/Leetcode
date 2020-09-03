# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # for each node return max(left_length, right_length) + 1
        if not root:
            return 0
        max_length = [0]
        self.max_path(root, max_length)
        return max_length[0] - 1

    def max_path(self, node, max_length):
        if not node:
            return 0
        left = self.max_path(node.left, max_length)
        right = self.max_path(node.right, max_length)
        prev_max = max_length.pop()
        max_length.append(max(prev_max, left + right + 1))
        return max(left, right) + 1
