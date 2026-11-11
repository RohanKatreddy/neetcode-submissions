class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        numberOfFresh = 0

        def add_cell(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in visited and grid[r][c] == 1:
                queue.append((r, c))
                visited.add((r, c))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: numberOfFresh += 1
                if grid[i][j] == 2:
                    for r, c in [(i + 1, j), (i - 1, j), (i, j+1), (i, j-1)]:
                        add_cell(r, c)

        timeElapsed = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                numberOfFresh -= 1
                for newR, newC in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
                    add_cell(newR, newC)
            timeElapsed += 1
        
        if numberOfFresh: return -1
        return timeElapsed

