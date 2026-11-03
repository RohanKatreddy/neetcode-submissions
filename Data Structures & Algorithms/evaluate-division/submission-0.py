class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, val in enumerate(equations):
            a, b = val
            graph[a].append((b, values[i]))
            graph[b].append((a, 1/values[i]))

        outputs = []
        for start, end in queries:
            if start not in graph or end not in graph: 
                outputs.append(-1.0)
                continue

            queue = deque()
            visited = set()
            queue.append((start, 1))
            scale_factor = -1.0
            while queue:
                node = queue.popleft()
                if node[0] in visited: continue
                visited.add(node[0])
                if node[0] == end:
                    scale_factor = node[1]
                    break
                
                for neighbour, weight in graph[node[0]]:
                    queue.append((neighbour, node[1] * weight))
            outputs.append(scale_factor)

        return outputs