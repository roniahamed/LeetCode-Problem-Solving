class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            st = str(i) 
            ln = len(st)
            if ln%2!=0:
                continue
            mid = ln//2
            first = st[mid:]
            second = st[:mid]
            left = sum(int(curr) for curr in first)
            right = sum(int(curr) for curr in second)
            if left == right:
                count += 1
        return count
                