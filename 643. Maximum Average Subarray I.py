class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k