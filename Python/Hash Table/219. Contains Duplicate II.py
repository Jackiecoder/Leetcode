class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hash map
        # Time O(n), space O(diff value)
        val_ind = {}
        for ind, val in enumerate(nums):
            if val in val_ind and ind - val_ind[val] <= k:
                return True
            val_ind[val] = ind
        return False

    def containsNearbyDuplicate_slidingWindow(self, nums: List[int], k: int) -> bool:
        # sliding window
        # length = k + 1
        # time O(n), space O(k)
        if len(nums) <= k + 1:
            return len(set(nums)) != len(nums)
        subarray = set(nums[:k + 1])
        if len(subarray) != k + 1:
            return True
        for i in range(k + 1, len(nums)):
            # add nums[i], remove nums[i - k - 1]
            subarray.remove(nums[i - k - 1])
            if nums[i] in subarray:
                return True
            subarray.add(nums[i])
        return False
