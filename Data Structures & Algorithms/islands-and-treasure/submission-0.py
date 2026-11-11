class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))

        def addCell(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] > 0:
                queue.append((r, c))
                visited.add((r, c))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                for newR, newC in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    addCell(newR, newC)
            distance += 1            