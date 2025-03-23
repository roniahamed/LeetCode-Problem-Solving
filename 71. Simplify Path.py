class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split('/')

        for pat in paths:
            if pat == '..':
                if stack:
                    stack.pop()
            elif pat and pat != '.':
                stack.append(pat)
        
        return '/' + '/'.join(stack)