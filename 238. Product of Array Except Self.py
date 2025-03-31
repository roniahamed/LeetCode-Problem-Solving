class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        answer = [1] * ln
        prefix = 1
        for i in range(ln):
            answer[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(ln-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer