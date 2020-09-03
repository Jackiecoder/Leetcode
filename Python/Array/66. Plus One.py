class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while index >= 0 and carry:
            digits[index] += carry
            carry = digits[index] // 10
            digits[index] %= 10
            index -= 1
        if carry:
            digits = [carry] + digits
        return digits
