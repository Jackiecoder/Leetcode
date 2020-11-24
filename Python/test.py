#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isCurrency' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING strAmount as parameter.
#

def isCurrency(strAmount):
    # 1. digit
    has_digit = False
    # 2. thousand separators
    has_thousand_separators = False
    # 3. prefix currency symbol
    is_Yen = False
    is_Euros_Dollar = False
    # 4. negative amounts
    has_negative_symbol = False
    has_left_parenthese = False
    has_right_parenthese = False
    # 5. cent
    has_decimal_point = False
    # 6. leading zero
    has_leading_zero = False

    count_digit = 0  # count digits in strAmount
    count_thousand_separator = 0  # count thousand separators in strAmount
    cent_digit_mark = 0  # mark how many digits before decimal point

    for i, c in enumerate(strAmount):
        # digit
        if c.isdecimal():
            if (not (is_Yen or is_Euros_Dollar)) or has_right_parenthese:
                return False

            count_digit += 1
            if not has_digit and c == '0':
                has_leading_zero = True
            has_digit = True
            continue

        # thousand separators
        if c == ',':
            if has_thousand_separators or (not has_digit) or (not (is_Yen or is_Euros_Dollar)) or has_right_parenthese or has_decimal_point:
                return False
            has_thousand_separators = True
            count_thousand_separator += 1
            continue

            # prefix currency symbol
            if c == '$' or c == '€':
                if has_digit or is_Euros_Dollar or is_Yen or has_decimal_point or has_right_parenthese or has_thousand_separators:
                    return False
                is_Euros_Dollar = True
                continue
            if c == '¥':
                if has_digit or is_Euros_Dollar or is_Yen or has_decimal_point or has_right_parenthese or has_thousand_separators:
                    return False
                is_Yen = True
                continue

            # negative amounts
            if c == '-':
                if i != 0:
                    return False
                has_negative_symbol = True
                continue
            if c == '(':
                if i != 0:
                    return False
                has_left_parenthese = True
                continue
            if c == ')':
                if has_right_parenthese or (i != len(strAmount) - 1):
                    return False
                has_right_parenthese = True
                continue

            # cent
            if c == '.':
                if is_Yen or (not is_Euros_Dollar) or (not has_digit) or has_decimal_point or has_right_parenthese:
                    return False
                has_decimal_point = True
                cent_digit_mark = count_digit
                continue

            return False

        # digit
        if not has_digit:
            return False

        # thousand separators
        if has_thousand_separators:
            if (cent_digit_mark // 3) != count_thousand_separator:
                return False

        # prefix
        if not (is_Yen or is_Euros_Dollar):
            return False

        # negative
        if has_negative_symbol and (has_left_parenthese or has_right_parenthese):
            return False
        if has_left_parenthese or has_right_parenthese:
            if not (has_left_parenthese and has_right_parenthese):
                return False

        # cent
        if is_Yen and has_decimal_point:
            return False
        if is_Euros_Dollar and has_decimal_point:
            if count_digit - cent_digit_mark != 2:
                return False

        # leading zero
        if has_leading_zero:
            if is_Yen:
                return False
            elif is_Euros_Dollar and count_digit != 3 and cent_digit_mark != 1:
                return False

        return True


if __name__ == '__main__':
    、
