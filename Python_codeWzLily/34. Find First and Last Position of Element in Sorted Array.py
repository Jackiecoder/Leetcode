class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # use binary search twice, to find left node and right node
        # Time O(logN), space O(1)

        # find left
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            left_node = left
        elif nums[right] == target:
            left_node = right
        else:
            return [-1, -1]

        # find right
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            right_node = right
        elif nums[left] == target:
            right_node = left
        else:
            return [-1, -1]
        return [left_node, right_node]
