class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # instead of sort each string, just count the frequency of each char, and make a array
        # e.g. 'eat' -> 100010000000....1000000
        # Time O(n + k), space O(26n) = O(n)
        hash_to_words = defaultdict(list)
        for string in strs:
            count_char = [0] * 26
            for char in string:
                count_char[ord(char) - ord('a')] += 1
            string_freq = ''
            for count in count_char:
                string_freq += str(count)
            hash_to_words[string_freq].append(string)
        return [val for val in hash_to_words.values()]

    def groupAnagrams_sortString(self, strs: List[str]) -> List[List[str]]:
        # hash table = { hash table = { char: times } : [eat, tea, ...]}
        # Time O(n * klogk), space O(n)
        hash_to_words = defaultdict(list)
        for string in strs:
            hash_to_words[tuple(sorted(string))].append(string)
        return list(map(list, hash_to_words.values()))
