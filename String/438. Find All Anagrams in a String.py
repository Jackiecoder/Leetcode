class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # assume len(s) = n, len(p) = m,
        # c = Counter(s[0:m]) -> compare with Counter(p)
        # if it is equal -> res.append(starter)
        # else: -> move on
        # c = {} -> empty ? append res
        # c = {}
        # i = 6
        # res = [0, 6]
        # time O(m + n), space O(n)

        n, m = len(s), len(p)
        res = []
        if m > n:
            return []
        c = defaultdict(int)
        for char in p:
            c[char] += 1
        for i in range(m):
            char = s[i]
            c[char] -= 1
            if c[char] == 0:
                c.pop(char)
        if not c:
            res.append(0)
        for i in range(1, n - m + 1):
            add = s[i + m - 1]
            delete = s[i - 1]
            c[add] -= 1
            if c[add] == 0:
                c.pop(add)
            c[delete] += 1
            if c[delete] == 0:
                c.pop(delete)
            if not c:
                res.append(i)
        return res
