class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 1. DFS/BFS reach each possible points, and find out if it can reach the target
        #                       (x, y)
        #                   /              \
        #           (x + y, y)               (x, y + x)
        #   `       /.      \.              /.          \
        #  (x + 2y, y) (x + y, x + 2y)  (2x+y, x+y)  (x, 2x+y)
        #   .....
        #   assume n = tx-sx, m = ty-sy
        #   Time O(mn), Space O(mn)

        # 2. From target back to the start point
        #       because each step, (x, y) -> (x, y+x) or (x+y, y)
        #     has [the larger one - the smaller one = the original number of larger one]
        # .      so I want to find the point will is equal to (x, y + kx) or (x + ky, y)
        while (tx > sx and ty > sy):
            if ty > tx:
                ty %= tx
            else:
                tx %= ty
        if (tx == sx and ty >= sy and (ty - sy) % sx == 0) or (ty == sy and tx >= sx and (tx - sx) % sy == 0):
            return True
        return False
