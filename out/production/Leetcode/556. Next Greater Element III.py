class Solution:
    def nextGreaterElement(self, n: int) -> int:
        string_n = list(str(n))
        last_smaller = -1
        mask = 2 ** 31 - 1
        for i in range(len(string_n) - 1):
            if string_n[i] < string_n[i + 1]:
                last_smaller = i
        if last_smaller == -1:
            return -1
        for j in range(last_smaller + 1, len(string_n)):
            if string_n[last_smaller] < string_n[j]:
                smallest_greater = j
        string_n[last_smaller], string_n[smallest_greater] = string_n[smallest_greater], string_n[last_smaller]
        string_n[last_smaller + 1:] = sorted(string_n[last_smaller + 1:])
        res = int(''.join(string_n))
        return res if res < mask else -1
