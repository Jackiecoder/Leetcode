class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = collections.deque()
        index = len(expression) - 1
        while index >= 0:
            char = expression[index]
            if char != '?':
                if char != ':':
                    stack.append(char)
                index -= 1
            else:
                condition = expression[index - 1]
                true_expression = stack.pop()
                false_expression = stack.pop()
                if condition == 'T':
                    stack.append(true_expression)
                else:
                    stack.append(false_expression)
                index -= 2
        return stack.pop()
