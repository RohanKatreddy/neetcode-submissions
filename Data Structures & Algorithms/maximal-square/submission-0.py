class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bottom up approach
        # DP matrix of zeros with shape of input matrix
        # Each position holds the size of largest square formed with it at the bottom right corner
        # for each position if it's one, then min(top and left) + 1
        dp_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == '0': continue
                top = dp_matrix[x-1][y] if x > 0 else 0
                left = dp_matrix[x][y-1] if y > 0 else 0
                diag = dp_matrix[x-1][y-1] if x > 0 and y > 0 else 0
                dp_matrix[x][y] = min(top, left, diag) + 1

        max_area = 0
        for row in dp_matrix:
            max_area = max(max_area, max(row))

        return max_area * max_area