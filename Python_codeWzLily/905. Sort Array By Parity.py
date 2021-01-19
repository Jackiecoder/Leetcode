class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # Time O(n), space O(1)
        odd = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[odd] = A[odd], A[i]
                odd += 1
        return A
