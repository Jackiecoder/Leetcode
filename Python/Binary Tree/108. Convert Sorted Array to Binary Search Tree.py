# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Time O(N), Space O(N)
        return self.sortedSubarrayToBST(nums, 0, len(nums) - 1)

    def sortedSubarrayToBST(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedSubarrayToBST(nums, l, mid - 1)
        root.right = self.sortedSubarrayToBST(nums, mid + 1, r)
        return root
