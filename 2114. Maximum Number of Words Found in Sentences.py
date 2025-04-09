class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_word = 0
        for  sentence in sentences:
            words = sentence.split()
            ln = len(words)
            max_word = max(ln, max_word)
        return max_word