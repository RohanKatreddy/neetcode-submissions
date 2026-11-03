class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            new_stone = abs(x - y)
            if new_stone: heapq.heappush(stones, -new_stone)

        return -stones[0] if len(stones) == 1 else 0