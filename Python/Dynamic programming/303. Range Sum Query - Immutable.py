class NumArray:

    def __init__(self, nums: List[int]):
        if nums:
            n = len(nums)
            sum_from_0_to_i = [0] * (n + 1)
            for i in range(1, n + 1):
                sum_from_0_to_i[i] = sum_from_0_to_i[i - 1] + nums[i - 1]
            self.sum_from_0_to_i = sum_from_0_to_i

    def sumRange(self, i: int, j: int) -> int:
        sum_from_0_to_i = self.sum_from_0_to_i
        return sum_from_0_to_i[j + 1] - sum_from_0_to_i[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
