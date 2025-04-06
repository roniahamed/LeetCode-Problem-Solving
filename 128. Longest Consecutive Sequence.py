
# Using Sorting 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ln = len(nums)
        if ln == 0:
            return 0
        if ln == 1:
            return 1
        nums = list(nums)
        nums.sort()
        count = 1
        max_count = 0
        for i in range(1,ln):
            if nums[i] - 1 == nums[i-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
        return max_count


# Using Set 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_count = 0
        count = 0
        for num in nums:
            if num-1 not in nums:
                count = 1
                current = num
                while current+1 in nums:
                    count += 1
                    current += 1
                max_count = max(max_count, count)
        
        return max_count
