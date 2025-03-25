class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) / 2 == sum(nums):
            return len(nums)
        max_length = 0
        sum_map = {0:-1}
        sum_num = 0
        for i, num in enumerate(nums):

            sum_num += 1 if num == 1 else -1

            if sum_num in sum_map:
                max_length = max(max_length, i-sum_map[sum_num])
            else:
                sum_map[sum_num] = i
        return max_length
