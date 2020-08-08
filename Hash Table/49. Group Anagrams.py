class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash table = { hash table = { char: times } : [eat, tea, ...]}
        # Time O(n * klogk), space O(n)
        hash_to_words = defaultdict(list)
        for string in strs:
            hash_to_words[tuple(sorted(string))].append(string)
        return list(map(list, hash_to_words.values()))
