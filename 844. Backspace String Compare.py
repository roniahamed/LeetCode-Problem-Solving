class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def check(word):
            stack = []
            for c in word:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return check(s) == check(t)