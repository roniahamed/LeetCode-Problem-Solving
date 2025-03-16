class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        l = len(nums)
        if l==1:
            return nums[0]
        max_sum = -100
        for i in range(l):
            for j in range(i+1,l+1):
                su = sum(nums[i:j])
                max_sum = max(su, max_sum)
        return max_sum