def sumOfTwoString(s1, s2):
    n, m = len(s1), len(s2)
    i, j = n - 1, m - 1
    res = ''
    while i >= 0 and j >= 0:
        res = str(ord(s1[i]) - ord('0') + ord(s2[j]) - ord('0')) + res
        i -= 1
        j -= 1
    while i >= 0:
        res = str(ord(s1[i]) - ord('0')) + res
        i -= 1
    while j >= 0:
        res = str(ord(s2[j]) - ord('0')) + res
        j -= 1
    return res


res = sumOfTwoString('4567', '678')
print(res)
