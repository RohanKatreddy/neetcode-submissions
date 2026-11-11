class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        temp = 0
        for i in range(len(nums)):
            temp = max(temp + nums[i], nums[i])
            best = max(best, temp)
        return best