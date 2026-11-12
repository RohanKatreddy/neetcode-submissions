class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != 'O': return
            board[x][y] = 'S'
            for offsetX, offsetY in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(x + offsetX, y + offsetY)


        for x in range(m):
            dfs(x, 0)
            dfs(x, n-1)
        for y in range(n):
            dfs(0, y)
            dfs(m-1, y)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 'S':
                    board[x][y] = 'O'
                else: board[x][y] = 'X'        