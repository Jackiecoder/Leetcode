class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # The equal row must be all of  A[0] or B[0]
        # The length = n:
        res = []
        for tgt in [A[0], B[0]]:
            res.append(self.equal_row(A, B, tgt))
            res.append(self.equal_row(B, A, tgt))
        min_res = [x for x in res if x >= 0]
        if min_res:
            return min(min_res)
        return -1

    def equal_row(self, A, B, tgt):
        steps = 0
        for i in range(len(A)):
            if A[i] == tgt:
                continue
            elif B[i] == tgt:
                steps += 1
            else:
                return -1
        return steps
