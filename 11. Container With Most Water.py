class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0
        while left < right:
            min_height = min(height[left], height[right])
            index = right - left
            max_water = max(max_water, index * min_height)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water