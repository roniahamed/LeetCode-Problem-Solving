# O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        if s_count == t_count:
            return True
        return False


# O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))
        if s == t:
            return True
        return False
        