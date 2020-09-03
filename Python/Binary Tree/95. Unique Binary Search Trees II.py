# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # divide and conquer
        if n <= 0:
            return []
        return self.generateSubtrees(1, n, {})

    def generateSubtrees(self, start, end, memo):
        # start and end are included
        if (start, end) in memo:
            return memo[(start, end)]
        if start > end:
            return [None]
        res = []
        for root_val in range(start, end + 1):
            left_subtrees = self.generateSubtrees(start, root_val - 1, memo)
            right_subtrees = self.generateSubtrees(root_val + 1, end, memo)
            for l_sub in left_subtrees:
                for r_sub in right_subtrees:
                    root = TreeNode(root_val, l_sub, r_sub)
                    res.append(root)
        memo[(start, end)] = res
        return res
