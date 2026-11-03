class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0: continue
                if (x, y) in visited: continue
                max_area = max(max_area, self._calculate_component_area(x, y, grid, visited))
        return max_area

        

    def _calculate_component_area(self, x, y, grid, visited):
        if not(0 <= x < len(grid)) or not(0 <= y < len(grid[0])):
            return 0
        if grid[x][y] == 0: return 0
        if (x, y) in visited: return 0

        visited.add((x, y))
        return (1 + self._calculate_component_area(x + 1, y, grid, visited)
                 + self._calculate_component_area(x - 1, y, grid, visited)
                 + self._calculate_component_area(x, y + 1, grid, visited)
                 + self._calculate_component_area(x, y - 1, grid, visited))