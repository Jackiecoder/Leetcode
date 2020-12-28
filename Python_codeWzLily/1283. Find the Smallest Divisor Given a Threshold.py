class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # binary search
        # bottom = 1, top = largest number in nums
        # Time O(n + n * logn) or O(n * log 10**6), space O(1)
        l, r = 1, max(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            ans = self.get_sum(nums, mid)
            if ans <= threshold:
                r = mid
            else:
                l = mid
        if self.get_sum(nums, l) <= threshold:
            return l
        return r

    def get_sum(self, nums, divisor):
        ans = 0
        for num in nums:
            ans += math.ceil(num / divisor)
        return ans
