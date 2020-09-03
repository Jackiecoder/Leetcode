class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Let's consider it without any characters
        # (()))
        # )()
        # 1. if we have right, and no un-paired left parentheses, remove this right parentheses
        #     e.g. ())
        # 2. if we reach the end of the string, and we find that we have more left parentheses than right parentheses --> remove left
        #    e.g. (()

        # Stack to solve it
        # left_stack = [0, 1] # index of left

        # Let's add characters to s
        # e.g. "lee(t(c)o)de)"
        # left_stack = []
        # i: 0 -> n - 1
        # i = 7
        # tmp_string = 'lee(t(c)o)de'
        # if '(' -> push tmp_string to stack, and empty it.
        # if ')' -> add  < stack.pop() + '(' + 'tmp' + ')'> to tmp.
        #        -> empty continue
        # time O(n), space O(n)

        # e.g. "a)b(c)d"
        # left_stack = []
        # i = 0
        # tmp_string = 'ab(c)d'

        stack = collections.deque()
        tmp = ''
        for i, char in enumerate(s):
            if char == '(':
                stack.append(tmp)
                tmp = ''
            elif char == ')':
                if not stack:
                    continue
                tmp = stack.pop() + '(' + tmp + ')'
            else:
                tmp += char
        return ''.join(stack) + tmp
