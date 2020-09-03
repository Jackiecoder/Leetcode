class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap[target - A[i]] = i
        # time O(n), space O(n)

        # two pointers
        # time O(n), space O(1)
        left, right = 0, len(numbers) - 1
        while left < right:
            ssum = numbers[left] + numbers[right]
            if ssum == target:
                return [left + 1, right + 1]
            elif ssum < target:
                left += 1
            else:
                right -= 1
        return []
