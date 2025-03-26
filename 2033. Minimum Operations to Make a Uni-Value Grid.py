class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = [num for row in grid for num in row]
        values.sort()
        mod_base = values[0] % x
        
        for value in values:
            if value % x != mod_base:
                return -1
        
        mid_value = values[len(values)//2]

        minimum_operation = sum(abs(mid_value-value)//x for value in values)
        return minimum_operation