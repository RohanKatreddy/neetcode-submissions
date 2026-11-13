class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        column = [True] * n
        diag1 = [True] * (n*2)
        diag2 = [True] * (n*2)

        grid = ['.' * n for _ in range(n)]

        def place(matrix, row):
            if row == n: return [[''.join(r) for r in matrix]]

            results = []
            for y in range(n):
                if (column[y] and diag1[y-row] and diag2[y+row]):
                    column[y] = diag1[y-row] = diag2[y+row] = False
                    matrix[row] = matrix[row][:y] + 'Q' + matrix[row][y+1:]                    
                    results.extend(place(matrix, row+1))
                    column[y] = diag1[y-row] = diag2[y+row] = True
                    matrix[row] = '.' * n
            
            return results

        return place(grid, 0)
