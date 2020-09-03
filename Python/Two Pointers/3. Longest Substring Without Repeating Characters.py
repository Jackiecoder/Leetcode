class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hashmap = {char: index}
        # "start" is where the non-repeating substring start
        char_index = {}
        max_length = 0
        start = 0
        for i, char in enumerate(s):
            if char in char_index and start <= char_index[char]:
                start = i + 1
            else:
                max_length = max(max_length, i - start + 1)
            char_index[char] = i + 1
        return max_length
