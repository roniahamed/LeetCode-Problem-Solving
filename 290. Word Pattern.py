class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        len_pattern = len(pattern)
        len_word = len(word)
        if len_pattern != len_word:
            return False
        unique_word = len(set(word))
        unique_pattern = len(set(pattern))
        if unique_word != unique_pattern:
            return False
        check = {}
        for i in range(len_word):
            if pattern[i] in check and word[i] != check[pattern[i]]:
                return False
            check[pattern[i]] = word[i]
        return True


""" Problem link: https://leetcode.com/problems/word-pattern/description/ """
""" Solution link: https://leetcode.com/problems/word-pattern/solutions/6558934/easy-solution-by-roniahamed-sj24 """