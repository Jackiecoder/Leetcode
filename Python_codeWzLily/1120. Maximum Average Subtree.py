# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        # post-order traverse
        #   [left], [right], node
        # if a node have no left and right node -> sum, num = val, 1
        # for other nodes, -> ave, num = left_sum + right_sum + val, (left_num + right_num + 1)
        # Time O(n), Space O(n)
        res = [0]
        self.dfs(root, res)
        return res[0]

    def dfs(self, root, res):
        if not root:
            return 0, 0
        total = root.val
        num = 1
        left_val, left_num = self.dfs(root.left, res)
        right_val, right_num = self.dfs(root.right, res)
        total += left_val + right_val
        num += left_num + right_num
        if res[0] < total / num:
            res.pop()
            res.append(total / num)
        return total, num
