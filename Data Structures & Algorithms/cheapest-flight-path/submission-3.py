class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = defaultdict(lambda: float('inf'))
        distances[src] = 0
        for _ in range(k+1):
            temp = distances.copy()
            for flight in flights:
                s, d, price = flight
                if distances[d] > temp[s] + price:
                    distances[d] = min(temp[d], temp[s] + price)
        return -1 if distances[dst] == float('inf') else distances[dst]