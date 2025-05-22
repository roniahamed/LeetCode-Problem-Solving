class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack =[]
        nums_map = {}
        ln = len(nums)
        result = [-1] * (ln*2)
        nums += nums
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result[:ln]