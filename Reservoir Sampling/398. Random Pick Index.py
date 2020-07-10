class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick_rand(self, target: int) -> int:
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                ran = random.randint(1, count)
                if ran == count:
                    res = i
        return res

    def pick(self, target):
        return random.choice([k for k, v in enumerate(self.nums) if v == target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
