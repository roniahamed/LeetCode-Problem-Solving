class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        size = len(strs) -1
        l = min(len(strs[0]), len(strs[size]))
        i = 0
        while i<l and strs[0][i] == strs[size][i]:
            i += 1
        
        return strs[0][:i]