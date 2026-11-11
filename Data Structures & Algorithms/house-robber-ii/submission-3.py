class Solution:
    def rob(self, nums: List[int]) -> int:

        self.memo = {}
        
        def dp(k, first_robbed):
            if (k, first_robbed) in self.memo: return self.memo[(k, first_robbed)]
            if k >= len(nums): return 0

            
            res = -1
            if first_robbed and k == len(nums) - 1: return 0
            elif first_robbed and k+1 >= len(nums) - 1: res = nums[k]
            elif first_robbed and k+2 >= len(nums) - 1: res = max(dp(k+1, first_robbed), nums[k])
            else: res =  max(dp(k+1, first_robbed), dp(k+2, first_robbed) + nums[k])

            self.memo[(k, first_robbed)] = res
            return self.memo[(k, first_robbed)]

        return max(dp(1, False), dp(2, True) + nums[0])