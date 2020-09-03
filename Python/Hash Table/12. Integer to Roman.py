ROMAN_DIC = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num:
            for val in sorted(ROMAN_DIC.keys(), reverse=True):
                for _ in range(num // val):
                    res += ROMAN_DIC[val]
                num %= val
        return res
