# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # T(n) = T(n - 1) + 2 * T(n - 2) + 3* T(n - 3) + ... + n* T(1)
        #       = (1 * n + 2 * (n - 1) + 3 * (n - 2) + .. + i * (n - i + 1))
        #       =
        # Space O(2 ^ n)
        if n == 0:
            return []
        return self.subtrees(1, n, {})

    def subtrees(self, start, end, memo):
        # return subtree with [start, end]
        if (start, end) in memo:
            return memo[(start, end)]
        if start > end:
            return [TreeNode(float('inf'))]
        if start == end:
            return [TreeNode(start)]
        res = []
        for root_val in range(start, end + 1):
            left_list = self.subtrees(start, root_val - 1, memo)
            right_list = self.subtrees(root_val + 1, end, memo)
            for l in left_list:
                for r in right_list:
                    root = TreeNode(root_val)
                    root.left = l if l.val != float('inf') else None
                    root.right = r if r.val != float('inf') else None
                    res.append(root)
        memo[(start, end)] = res
        return res
