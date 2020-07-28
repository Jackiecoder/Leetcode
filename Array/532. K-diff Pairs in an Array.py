class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # set(nums)
        # for each num in nums -> find num + k
        #   once reached -> add used
        if k < 0:
            return 0
        counter = Counter(nums)
        count_pair = 0
        for num in counter.keys():
            counter[num] -= 1
            if num + k in counter and counter[num + k] > 0:
                count_pair += 1
            counter[num] += 1
        return count_pair
