class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # move each number to end
        # time O(n ** 2)
        end = len(arr) - 1
        res = []
        while end >= 0:
            target = end + 1
            ind = arr.index(target)
            arr[:ind + 1] = arr[:ind + 1][::-1]
            arr[:end + 1] = arr[:end + 1][::-1]
            res.append(ind + 1)
            res.append(end + 1)
            end -= 1
        return res
