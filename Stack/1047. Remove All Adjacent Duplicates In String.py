class Solution:
    def removeDuplicates(self, S: str) -> str:
        # use a stack to store all element:
        # if cur char == stack top
        #   pop out
        # assume n = len(S):
        # time O(n), space O(n)

        stack = []
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
