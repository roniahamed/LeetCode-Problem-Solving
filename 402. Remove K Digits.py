class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = stack[:-k] if k else stack
        result = ''.join(stack).lstrip('0')
        return result if result else '0'