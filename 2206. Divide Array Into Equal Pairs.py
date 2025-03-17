class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for val in counter.values():
            if val%2==1:
                return False

        return True


/* 
Problem link: https://leetcode.com/problems/divide-array-into-equal-pairs/
solution link: https://leetcode.com/problems/divide-array-into-equal-pairs/solutions/6545880/best-solution-this-question 
*/ 
