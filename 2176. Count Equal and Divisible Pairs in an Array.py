class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ln = len(nums)
        count = 0
        for i in range(ln):
            for j in range(i+1, ln):
                if nums[i] == nums[j]:
                    val = i * j
                    if val % k == 0:
                        count += 1
        return count
