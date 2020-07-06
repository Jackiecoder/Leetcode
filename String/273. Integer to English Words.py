DIC = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
    102: "Hundred",
    103: "Thousand",
    106: "Million",
    109: "Billion"
}


class Solution:
    def numberToWords(self, num: int) -> str:
        # 1,234,567
        # 1 -> One + Billion
        # 234 -> two hundred thirty four + Thousand
        # 567 -> five hundred sixty seven + ''
        res = []
        for times in [9, 6, 3]:
            if num >= 10 ** times:
                self.three_digits(num // 10 ** times, res)
                res.append(DIC[100 + times])
                num %= 10 ** times
        self.three_digits(num, res)
        return ' '.join(res)

    def three_digits(self, num, res):
        if num == 0 and not res:
            res.append(DIC[num])
            return
        if 100 <= num < 1000:
            res.append(DIC[num // 100])
            res.append(DIC[102])
            num %= 100
        if 20 <= num < 100:
            res.append(DIC[num // 10 * 10])
            num %= 10
        if 0 < num < 20:
            res.append(DIC[num])
