class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] == 0 :
                nums [i] ^= 1
                nums [i+1] ^= 1
                nums [i+2] ^= 1
                count += 1
        if nums[-1] == nums[-2] == 1:
            return count
        return -1
