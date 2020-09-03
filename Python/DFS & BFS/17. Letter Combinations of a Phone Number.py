class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs
        # each level -> 3 * len(cur_res)
        # Time O(a ^ n) -> a is average number of letters, Space O(1)
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        return self.subletterCombinations(digits, 0, dic)

    def subletterCombinations(self, digits, index, dic):
        if index == len(digits):
            return ['']
        head = digits[index]
        remain = self.subletterCombinations(digits, index + 1, dic)
        res = []
        for char in dic[head]:
            for tmp in remain:
                res.append(char + tmp)
        return res
