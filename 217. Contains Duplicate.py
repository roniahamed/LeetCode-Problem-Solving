class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        has_map = {}
        for num in nums:
            if num in has_map:
                return True
            has_map[num] = 1
        return False