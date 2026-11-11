class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificVisited = set()
        atlanticVisited = set()

        queue = deque()
        for r in range(len(heights)):
            queue.append((r, 0))
            pacificVisited.add((r, 0))
        for c in range(1, len(heights[0])):
            queue.append((0, c))
            pacificVisited.add((0, c))

        def add_cell(r, c, prev):
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and (r, c) not in pacificVisited and heights[r][c] >= prev:
                queue.append((r, c))
                pacificVisited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for newR, newC in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
                    add_cell(newR, newC, heights[r][c])
        
        
        result = []
        for r in range(len(heights)):
            queue.append((r, len(heights[0]) - 1))
            atlanticVisited.add((r, len(heights[0]) - 1))
        for c in range(len(heights[0]) - 1):
            queue.append((len(heights) - 1, c))
            atlanticVisited.add((len(heights) - 1, c))


        def add_cell(r, c, prev):
            if 0 <= r < len(heights) and 0 <= c < len(heights[0]) and (r, c) not in atlanticVisited and heights[r][c] >= prev:
                queue.append((r, c))
                atlanticVisited.add((r, c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) in pacificVisited: result.append((r, c))
                for newR, newC in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
                    add_cell(newR, newC, heights[r][c])

        return result
