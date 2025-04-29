class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        s1 = Counter(s1)
        count = Counter(s2[:len_s1])
        if count == s1:
            return True
        left = 0
        for right in range(len_s1, len(s2)):
            count[s2[left]] -= 1
            count[s2[right]] += 1
            left += 1
            if s1 == count:
                return True
        return False