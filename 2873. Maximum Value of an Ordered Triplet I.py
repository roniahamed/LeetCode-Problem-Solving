# O(n)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        triplet = 0
        triplet_i = 0
        for num in nums :
            answer = max(answer, triplet * num)
            triplet = max(triplet_i - num, triplet )
            triplet_i = max(triplet_i, num)
           
        return answer


# O(n^2)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        max_triplet_j = nums[0]
        ln = len(nums)
        for i in range(1,ln):
            max_triplet_j = max(max_triplet_j, nums[i-1])
            for j in range(i+1, ln):
                curr_triplet = (max_triplet_j - nums[i]) * nums[j]
                if curr_triplet > max_triplet:
                    max_triplet = curr_triplet
        return max_triplet

# O(n^3)

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_triplet = 0
        ln = len(nums)
        for i in range(ln):
            for j in range(i+1, ln):
                for k in range(j+1, ln):
                    curr_triplet = (nums[i]-nums[j]) * nums[k]
                    if max_triplet < curr_triplet:
                        max_triplet = curr_triplet
        return max_triplet