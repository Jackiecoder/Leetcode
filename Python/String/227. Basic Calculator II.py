class Solution:
    def calculate(self, s: str) -> int:
        #       3 + 2 * 2
        #   -> 5 * 2 -> 3 + 2 * 2 = 7
        #       3 - 2 * 2
        #   -> 1 * 2 -> 3 + ( -2 * 2) = -1
        # Time O(n), space O(1)
        ind = 0
        num = 0
        while ind < len(s) and s[ind] not in ['+', '-', '*', '/']:
            if s[ind] != ' ':
                num = num * 10 + int(s[ind])
            ind += 1
        return self.calSub(s, ind, num, num)

    def calSub(self, s, ind, accu, prev):
        # print(accu, prev)
        if ind == len(s):
            return accu
        oper = s[ind]
        ind += 1
        num = 0
        while ind < len(s) and s[ind] not in ['+', '-', '*', '/']:
            if s[ind] != ' ':
                num = num * 10 + int(s[ind])
            ind += 1
        if oper == '+':
            return self.calSub(s, ind, accu + num, num)
        elif oper == '-':
            return self.calSub(s, ind, accu - num, -num)
        elif oper == '*':
            return self.calSub(s, ind, accu - prev + prev * num, prev * num)
        elif oper == '/':
            tmp = prev // num if prev >= 0 else -(-prev // num)
            return self.calSub(s, ind, accu - prev + tmp, tmp)
