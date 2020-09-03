class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # A [as1, ae1], [as2, as2]
        # B [bs1, be1], [bs2, be2]
        # two pointer to solve it
        # A -----------
        # B   --  ---
        # compare end, smaller one will move forward
        # interval = [max(Astart, Bstart), min(Aend, Bend)]
        #
        # e.g.
        # A = [[0,2],[5,10],[13,23],[24,25]]
        # B = [[1,5],[8,12],[15,24],[25,26]]
        # a_pointer = 3
        # b_pointer = 3
        # interval  =
        # res = [[1,2], [5,5], [8,10], [15, 23], [24,24], [25,25]]
        # time O(n + m), space O(n + m)
        # . --------   ----   -----
        # .  -- -    ----
        ap, bp = 0, 0
        res = []
        while ap < len(A) and bp < len(B):
            a_start, a_end = A[ap]
            b_start, b_end = B[bp]
            left = max(a_start, b_start)
            right = min(a_end, b_end)
            if left <= right:
                res.append([left, right])
            if a_end < b_end:
                ap += 1
            elif a_end > b_end:
                bp += 1
            else:
                ap += 1
                bp += 1
        return res
