class Solution:
    def minWindow(self, s: str, t: str) -> str:
        remain = set(t)
        start, end = 0, 0
        count = collections.Counter(t)
        min_range = [-float('INFINITY'), float('INFINITY')]
        # the rule is,  S[i] = char,
        #   count[char] -= 1 if count[char] <= 0 -> we have more char than our requirements
        #   remain remove char
        #       if remain is empty: -> this substring meet our requirment
        #   then we move start forward
        #       if start
        #           if count[char] > 0 -> remain.add(char)
        for end, char in enumerate(s):
            # print(start, end, count, remain)
            if char not in count:
                continue
            count[char] -= 1
            if count[char] <= 0:
                if char in remain:
                    remain.remove(char)
                while not remain:
                    if end - start < min_range[1] - min_range[0]:
                        min_range = [start, end]
                    start += 1
                    drop_char = s[start - 1]
                    if drop_char in count:
                        count[drop_char] += 1
                        if count[drop_char] > 0:
                            remain.add(drop_char)
        return s[min_range[0]: min_range[1] + 1] if min_range[0] >= 0 else ""
