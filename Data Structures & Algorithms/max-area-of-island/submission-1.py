class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0: continue
                max_area = max(max_area, self._calculate_component_area(x, y, grid))
        return max_area

        

    def _calculate_component_area(self, x, y, grid):
        if not(0 <= x < len(grid)) or not(0 <= y < len(grid[0])):
            return 0
        if grid[x][y] == 0: return 0

        grid[x][y] = 0
        return (1 + self._calculate_component_area(x + 1, y, grid)
                 + self._calculate_component_area(x - 1, y, grid)
                 + self._calculate_component_area(x, y + 1, grid)
                 + self._calculate_component_area(x, y - 1, grid))