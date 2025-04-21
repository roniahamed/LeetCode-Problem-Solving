class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_ln = len(p)
        if p_ln > len(s):
            return []
        p = Counter(p)
        anagram = []
        window_counter = Counter(s[:p_ln])
        if window_counter == p:
            anagram.append(0)
        for i in range(1, len(s)-p_ln+1):
            window_counter[s[i-1]] -= 1
            window_counter[s[i+p_ln-1]] += 1
            if window_counter == p:
                anagram.append(i)
        return anagram
            