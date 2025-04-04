class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store_anagram = {}
        for char in strs:
            sorted_char = ''.join(sorted(char))
            if sorted_char not in store_anagram:
                store_anagram[sorted_char] = []
            store_anagram[sorted_char].append(char)
        group_anagram = list(store_anagram.values())
        return group_anagram