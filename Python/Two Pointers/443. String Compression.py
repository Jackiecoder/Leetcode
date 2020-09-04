class Solution:
    def compress(self, chars: List[str]) -> int:
        # two pointers
        # pointer1 -> char
        # pointer2 -> find
        #
        # cur        = 0
        # char_index = 0
        # index      = 2
        # res = []

        # Time O(n), space O(1)
        cur = index = 0
        while index < len(chars):
            char = chars[index]
            start = index
            while index < len(chars) - 1 and chars[index] == chars[index + 1]:
                # index -> last index of this char
                index += 1
            chars[cur] = char
            if start != index:
                times = index - start + 1
                for i in str(times):
                    cur += 1
                    chars[cur] = i
            cur += 1
            index += 1
        return cur
