class SparseVector:
    # time O(2n + m), space O(2m)
    # n = len(vec), m = len(valid numbers)

    def __init__(self, nums: List[int]):
        self.vec = defaultdict(int)
        for i, num in enumerate(nums):
            if num == 0:
                continue
            self.vec[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        vec1, vec2 = self.vec, vec.vec
        if len(vec1) > len(vec2):
            vec1, vec2 = vec2, vec1  # make vec1 shorter

        for ind, num in vec1.items():
            if ind not in vec2:
                continue
            res += num * vec2[ind]
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
