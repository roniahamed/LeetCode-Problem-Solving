class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        store = []
        for i,word in enumerate(words):
            if x in word:
                store.append(i)
        return store