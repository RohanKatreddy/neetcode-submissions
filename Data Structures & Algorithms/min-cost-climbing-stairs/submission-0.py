class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = defaultdict(int)
        target = len(cost)
        return min(self._calculate(cost, 0, target), self._calculate(cost, 1, target))

    def _calculate(self, cost, i, target):
        if i > target: return float('inf')
        if i == target: return 0
        if i in self.memo: return self.memo[i]
        answer = cost[i] + min(self._calculate(cost, i + 1, target), 
                               self._calculate(cost, i + 2, target))
        self.memo[i] = answer
        return answer