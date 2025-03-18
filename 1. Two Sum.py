class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has_map = {}
        for i in range(len(nums)):
            has_map[nums[i]] = i
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in has_map and has_map[curr] != i:
                return [i,has_map[curr]]
        return []