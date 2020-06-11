class Solution:
    def calculate(self, s: str) -> int:
        # I will use num_stack to store the number on the left of operator
        #    and use opr_stack to store the operator
        # when reach (
        # and pop them when reach )
        # num_stack = []
        # opr_stack = []
        # cur_num = None
        # cur_opr =

        num_stack = collections.deque()
        opr_stack = collections.deque()
        cur_num, cur_opr = None, None
        mask = 2147483640
        index = 0
        while index < len(s):
            char = s[index]
            if char == ' ':
                pass
            elif char == '(':
                if cur_num is not None and cur_opr:
                    num_stack.append(cur_num)
                    opr_stack.append(cur_opr)
                    cur_num = None
                    cur_opr = None
            elif char in ['+', '-', '*', '/']:
                cur_opr = char
            elif char == ')':
                if num_stack and opr_stack:
                    cur_num = self.operation(
                        num_stack.pop(), cur_num, opr_stack.pop())
                    cur_opr = None
            else:
                string = ''
                while index < len(s) and '0' <= s[index] <= '9':
                    string = string + s[index]
                    index += 1
                if cur_opr:
                    cur_num = self.operation(cur_num, int(string), cur_opr)
                    cur_opr = None
                else:
                    cur_num = int(string)
                index -= 1
            index += 1
        return cur_num

    def operation(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        else:
            return num1 - num2
