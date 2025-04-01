## Prefix Sum:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        prefix  = 0
        min_prefix = 0
        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - min_prefix)
            min_prefix = min(prefix, min_prefix)
        return max_sum


## Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum