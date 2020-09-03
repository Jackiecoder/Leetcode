class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # freq of each char in p
        # and compare the freq with each k length substring in s
        # e.g. p -> {a:1, b:1, c:1}
        #   head = 1
        #   freq = {c:0, b:1, a:1, e:1}
        #   res = [0, ]
        # travel through the string,
        #    add s[i + length] + 1, and s[i - 1] - 1
        #    if freq[any key] == 0 -> remove this key
        # Time O(n), space O(k)
        n, k = len(s), len(p)
        freq_p = Counter(p)
        freq_s = defaultdict(int)
        for char in s[:k]:
            freq_s[char] += 1
        res = []

        for i in range(len(s) - k + 1):
            if i > 0:
                freq_s[s[i + k - 1]] += 1
                freq_s[s[i - 1]] -= 1
                if freq_s[s[i - 1]] == 0:
                    freq_s.pop(s[i - 1])
            if freq_s == freq_p:
                res.append(i)
        return res
