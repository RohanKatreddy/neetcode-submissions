class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sorted_points = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(sorted_points, (distance, point))

        closest = []        
        for _ in range(k):
            closest.append(heapq.heappop(sorted_points)[1])

        return closest