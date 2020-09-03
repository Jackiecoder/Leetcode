class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            elif char in pairs.values():
                if not stack or char != pairs[stack[-1]]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
