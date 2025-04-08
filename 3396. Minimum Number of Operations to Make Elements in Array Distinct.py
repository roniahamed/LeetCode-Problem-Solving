class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        ln = len(nums)
        if ln == len(set(nums)):
            return 0
        while True:
            count += 1
            ln -= 3
            if ln == len(set(nums[-ln:])) or ln <= 1:
                return count