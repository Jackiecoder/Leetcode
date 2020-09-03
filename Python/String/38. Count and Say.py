class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for _ in range(n - 1):
            tmp = ''
            count = 1
            number = res[0]
            for i in range(1, len(res)):
                if number != res[i]:
                    tmp += str(count) + number
                    count = 1
                    number = res[i]
                else:
                    count += 1
            tmp += str(count) + number
            res = tmp
        return res
