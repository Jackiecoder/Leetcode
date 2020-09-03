class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if token is operator, we will find last two nums  and do operation.
        # so we can use stack to store those numbers
        # ["4", "13", "5", "/", "+"]
        # stack = [4, 2.6]
        # time O(n), space O(n)

        stack = collections.deque()
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    tmp = first / second
                    if tmp > 0:
                        tmp = int(tmp)
                    else:
                        tmp = -int(-tmp)
                    stack.append(tmp)
            else:
                stack.append(int(token))
        return stack.pop()
