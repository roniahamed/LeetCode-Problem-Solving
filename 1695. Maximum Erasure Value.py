class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = {}
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        left = 0
        result = 0
        for i,v in enumerate(nums):
            if v in window and window[v] >= left:
                left = window[v] + 1
            window[v] = i
            curr = prefix[i]- prefix[left - 1] if left != 0 else prefix[i]
            if curr > result:
                result = curr
        return result
            

