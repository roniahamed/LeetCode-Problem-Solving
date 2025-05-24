class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        ln = len(heights)
        for i in range(ln+1):
            curr_h = 0 if i == ln else heights[i]
            while stack and curr_h < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area