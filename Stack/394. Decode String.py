class Solution:
    def decodeString(self, s: str) -> str:
        # 1 stack to solve it

        # revise s -> "1[" + s + "]"
        # e.g.  3[a]2[bc] -> 1[3[a2[bc]2c]]
        # num_stack = [1, 3]
        # res_string =  a bcbc cc
        # cur_num    =
        # cur_string =
        # when ] ->
        # s = "1[" + s + "]"
        cur_num, cur_string = '', ''
        stack = collections.deque()
        for char in s:
            if char.isdigit():
                cur_num += char
            elif char.isalpha():
                cur_string += char
            elif char == '[':
                stack.append((int(cur_num), cur_string))
                cur_num, cur_string = '', ''
            else:
                repeat, prev_string = stack.pop()
                cur_string = prev_string + repeat * cur_string
        return cur_string
