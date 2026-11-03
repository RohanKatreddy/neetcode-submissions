from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = defaultdict(int)
        return self._calculate(n)

    def _calculate(self, n):
        if n < 0: return 0
        if n == 0: return 1
        if n in self.memo: return self.memo[n]
        answer = self._calculate(n-1) + self._calculate(n-2)
        self.memo[n] = answer
        return answer