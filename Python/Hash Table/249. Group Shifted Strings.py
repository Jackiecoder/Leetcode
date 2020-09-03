class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # hash map to store all difference : ["abc"]
        # e.g. "abc" -> (1, 1)
        #       "bcd" -> (1, 1)
        #       "acef" -> (2, 2, 1)
        #       "xyz" -> (1, 1)
        #       "az" -> (25)
        #       "ba" -> (-1) + 26 -> (25)
        #       "a" -> ()
        #       "z" -> ()
        diff_str = defaultdict(list)
        for string in strings:
            if len(string) == 1:
                diff_str['one'].append(string)
                continue
            diffs = []
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i - 1])
                while diff < 0:
                    diff += 26
                diffs.append(diff)
            diff_str[tuple(diffs)].append(string)
        return list(diff_str.values())
