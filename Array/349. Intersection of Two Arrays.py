class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Follow up: Could you do it with time O(n), Space O(1)? assuming input arrays are sorted
        #           (resulting array not taken into consideration)
        # Algo:
        #   two pointers:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        res = []
        while i < m and j < n:
            if i > 0 and nums1[i] == nums1[i - 1]:
                i += 1
                continue
            if 0 < j and nums2[j] == nums2[j - 1]:
                j += 1
                continue
            if not i < m and j < n:
                break
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res

    def intersection_setIntersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time O(min(len(nums1), len(nums2))), Space O(n + m)
        return list(set(nums1).intersection(set(nums2)))

    def intersection_counter(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # count number and frequency in each array
        # res add minimum of each number's frequency
        # Time O(n), space O(n)
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = []
        for num in counter1:
            if num in counter2:
                res.append(num)
        return res
