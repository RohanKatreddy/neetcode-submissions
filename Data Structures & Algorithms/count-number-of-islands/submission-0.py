class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    if (x, y) not in self.visited:
                        count += 1
                        self._calculate(grid, x, y)

        return count


    def _calculate(self, grid, x, y):
        if not(0 <= x < len(grid)) or not(0 <= y < len(grid[0])): return
        if (x, y) in self.visited: return
        if grid[x][y] == "1": self.visited.add((x,y))
        else: return
        self._calculate(grid, x+1, y)
        self._calculate(grid, x-1, y)
        self._calculate(grid, x, y+1)
        self._calculate(grid, x, y-1)