class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_count = 0
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_count = max(max_count, i - stack[-1])
                else:
                    stack.append(i)

        return max_count