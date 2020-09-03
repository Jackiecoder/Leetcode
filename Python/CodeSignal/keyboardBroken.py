def keyboardBroken(string, charArray):
    word_set = string.split(' ')
    charArray = set(charArray)
    count_valid = 0
    for word in word_set:
        word_valid = True
        for char in word:
            if char.isalpha() and not char.lower() in charArray:
                word_valid = False
                break
        if word_valid:
            count_valid += 1
    return count_valid


input = "Hello, my dear friend!"
b = {'h', 'e', 'l', 'm', 'o', 'y'}
res = keyboardBroken(input, b)
print(res)
