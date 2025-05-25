class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ln = len(matrix[0])
        histogram = [0] * ln
        max_area = 0
        for m in matrix:
            for i in range(ln):
                histogram[i] = histogram[i] + 1 if m[i] == '1' else 0
            max_area = max(max_area, self.large_area_histogram(histogram, ln))
        return max_area
    def large_area_histogram(self, heights, ln):
        stack = []
        max_area = 0
        
        for i in range(ln+1):
            curr_height = 0 if ln == i else heights[i]
            while stack and curr_height < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area