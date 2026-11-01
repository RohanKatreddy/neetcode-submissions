class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        step_size = len(nums)//2
        k = 0
        while step_size > 0:
            if k + step_size < len(nums) and nums[k + step_size] > nums[0]:
                k += step_size
            else: step_size//=2
        
        return nums[k+1]