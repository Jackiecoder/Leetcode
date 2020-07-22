class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack store (char, times)
        # if times + 1 == k:
        #   pop
        # [(d,1), (e,3)]
        # time O(n), space O(n)
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                _, times = stack.pop()
                if times + 1 < k:
                    stack.append((char, times + 1))
            else:
                stack.append((char, 1))
        res = ''
        for char, t in stack:
            res += char * t
        return res
