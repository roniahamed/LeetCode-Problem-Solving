class Solution:
    def trap(self, height: List[int]) -> int:
        water_trap = 0
        max_previous = 0
        left = 0
        right = len(height) -1
        while left < right:
            min_current = min(height[left], height[right])
            max_previous = max(max_previous, min_current)
            water_trap += max_previous - min_current
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
        return water_trap