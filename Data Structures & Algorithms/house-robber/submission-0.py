class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = defaultdict(int)
        return self._calculate(nums, 0)

    def _calculate(self, nums, index):
        if index >= len(nums): return 0
        if index in self.memo: return self.memo[index]
        maximum_amount = max(self._calculate(nums, index + 1), self._calculate(nums, index+2) + nums[index])
        
        self.memo[index] = maximum_amount
        return maximum_amount