class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        n = len(nums)-1
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n
            while left < right:
                su = nums[i] + nums[left] + nums[right]
                if su == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    continue
                if su > 0:
                    right -= 1
                else:
                    left += 1
        triplets = list(triplets)
        return triplets