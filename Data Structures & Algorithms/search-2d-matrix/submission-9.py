class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while(l < r):
            mid = (l + r)//2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        mid = (l + r)//2
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            row = matrix[mid]
            step_size = len(row)//2
            start = 0
            while (step_size > 0):
                if start+step_size < len(row) and row[start+step_size] <= target:
                    start += step_size
                else: step_size//=2
            if row[start] == target: return True
            else: return False 
        else:
            return False