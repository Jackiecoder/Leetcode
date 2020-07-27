class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # two pointer (sliding window)
        # record the rightmost index of each character
        # for each char in S, update the right to the rightmost
        # if there is an intersection between two sequence, when we travel through S, there must be one i that i == right
        rightmost = {char: i for i, char in enumerate(S)}
        left, right = 0, 0
        res = []
        for i, char in enumerate(S):
            right = max(right, rightmost[char])
            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res

    def partitionLabels_hashTable(self, S: str) -> List[int]:
        # hash table
        # "ababcbacadefegdehijhklij"
        #  012345678901234567890123
        # {a:[0, 8], b:[1,5], c: [4,7], d:[9, 14], e:[10, 15], f:[11, 11],
        #  g:[13,13], h:[16,19], i:[17:22], j:[18:23], k:[20, 20],}
        # -------------
        #   ----   ---
        #                -----
        # start: 9
        # end :  15
        # -------
        # .   -------
        # time O(n + clogc), space O(n)

        char_to_index = defaultdict(list)
        for i, char in enumerate(S):
            char_to_index[char].append(i)
        indexs = sorted(char_to_index.values(), key=lambda x: x[0])

        start, end = indexs[0][0], indexs[0][-1]
        res = []
        for index in indexs:
            head, tail = index[0], index[-1]
            if head <= end:
                end = max(tail, end)
            else:
                res.append(end - start + 1)
                start = head
                end = tail
        res.append(end - start + 1)
        return res
