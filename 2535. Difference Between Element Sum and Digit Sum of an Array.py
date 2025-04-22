class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        nums_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            for val in str(num):
                digit_sum += int(val)
        return nums_sum - digit_sum