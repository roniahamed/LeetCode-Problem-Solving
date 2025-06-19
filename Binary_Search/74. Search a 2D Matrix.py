class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) 
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            col = mid % n
            row = mid // n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] >= target:
                right = mid -1
            else:
                left = mid + 1

        return False