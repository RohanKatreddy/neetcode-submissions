class Solution:
    def rob(self, nums: List[int]) -> int:

        self.memo = {}
        
        def dp(k, first_robbed):
            if (k, first_robbed) in self.memo: return self.memo[(k, first_robbed)]
            if k >= len(nums): return 0
            if first_robbed and k == len(nums) - 1: return 0

            

            self.memo[(k, first_robbed)] = max(dp(k+1, first_robbed), dp(k+2, first_robbed) + nums[k])

            return self.memo[(k, first_robbed)]

        return max(dp(1, False), dp(2, True) + nums[0])