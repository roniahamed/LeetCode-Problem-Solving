class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(sub):
            if sub == sub[::-1]:
                return True
            return False
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return palindrome(s[left:right]) or palindrome(s[left+1:right+1])
            left += 1
            right -= 1
        return True