class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjacency_list = defaultdict(list)

        for i, val in enumerate(equations):
            start, end = val
            scale_factor = values[i]
            adjacency_list[start].append((end, scale_factor))
            adjacency_list[end].append((start, 1/scale_factor))


        def dfs(node, end, accumulated, visited):
            if node in visited: return -1
            visited.add(node)
            if node == end:
                return accumulated
            for neighbour, scale in adjacency_list[node]:
                value = dfs(neighbour, end, accumulated * scale, visited)
                if value != -1: return value
            return -1


        output = []
        for start, end in queries:
            if start not in adjacency_list or end not in adjacency_list:
                output.append(-1)
                continue

            queue = deque()
            queue.append((start, 1))
            visited = set()
            answer = dfs(start, end, 1, visited)

            output.append(answer)

        return output