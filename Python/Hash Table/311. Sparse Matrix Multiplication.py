class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # A_x = [0, 1, 1]
        # A_y = [0, 0, 2]
        # Aval= [1, -1, 3]

        # B_x = [0, 2]
        # B_y = [0, 2]
        # Bval= [7, 1]

        # for any (x, y) we need to find A[x, :] * B[:, y]
        # A = {
        #   0: {0: 1},
        #   1: {0: -1, 2: 3}
        #   }
        # B = {
        #   0: {0 : 7}
        #   1: {}
        #   2: {2: 1}
        # }
        # so for res[i][j] = sum(product of same key in A[i] and B[j])
        #  res = [[ 7, 0, 0], [ -7, 0, 3]]
        # A (n, m), B(m, k)
        # Time O(nm + mk + nk), Space O(nk)
        a_dic, b_dic = defaultdict(dict), defaultdict(dict)
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    a_dic[i].update({j: A[i][j]})
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] != 0:
                    b_dic[j].update({i: B[i][j]})
        res = [[0] * len(B[0]) for _ in range(len(A))]
        for row in a_dic:
            for col in b_dic:
                for valid_index in a_dic[row]:
                    if valid_index in b_dic[col]:
                        res[row][col] += a_dic[row][valid_index] * \
                            b_dic[col][valid_index]
        return res
