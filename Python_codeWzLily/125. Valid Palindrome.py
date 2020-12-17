class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer
        # compare s[i] and s[j]
        #   if same: i + 1, j - 1
        #       else: return False
        # Time O(n), space O(1)
        start, end = 0, len(s) - 1
        while start < end:
            head, tail = s[start], s[end]
            if not head.isalnum():
                start += 1
                continue
            if not tail.isalnum():
                end -= 1
                continue
            if head.lower() != tail.lower():
                return False
            start += 1
            end -= 1
        return True
