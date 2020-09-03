class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        123 * 456 -> 
        res[0] = 3 * 6 = 18
        res[1] = 3 * 5 + 2 * 6 = 27  -> add the carry 1 in res[0] -> 28
        res[2] = 12 + 10 + 6 = 28  -> add the carry 2 in res[1] -> 30
        res[3] = 8 + 5 = 13 -> add the carry 3 -> 16
        res[4] = 4 -> add carry 1 -> 5
        ---> 56088

        Time O(n * m + m + n)
        '''
        if num1 == '0' or num2 == '0':
            return '0'
        products = [0] * (len(num1) + len(num2))
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                products[i + j] += int(c1) * int(c2)
        res = ''
        carry = 0
        for i in range(len(products)):
            num = products[i] + carry
            res = str(num % 10) + res
            carry = num // 10
        index = 0
        while res[index] == '0':
            index += 1
        return res[index:]
