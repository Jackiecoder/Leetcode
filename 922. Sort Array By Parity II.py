class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = 0
        for odd in range(1, len(A), 2):
            if A[odd] % 2 == 1:
                continue
            while even < len(A) and A[even] % 2 == 0:
                even += 2
            A[odd], A[even] = A[even], A[odd]
        return A
