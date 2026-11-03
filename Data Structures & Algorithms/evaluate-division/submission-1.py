class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjacency_list = defaultdict(list)

        for i, val in enumerate(equations):
            start, end = val
            scale_factor = values[i]
            adjacency_list[start].append((end, scale_factor))
            adjacency_list[end].append((start, 1/scale_factor))

        output = []
        for start, end in queries:
            if start not in adjacency_list or end not in adjacency_list:
                output.append(-1)
                continue

            queue = deque()
            queue.append((start, 1))
            answer = -1
            visited = set()

            while queue:
                node, accumulated_scale_factor = queue.popleft()
                if node in visited: continue
                if node == end:
                    answer = accumulated_scale_factor
                    break
                
                visited.add(node)
                for neighbour, scale_factor in adjacency_list[node]:
                    queue.append((neighbour, accumulated_scale_factor * scale_factor))

            output.append(answer)

        return output